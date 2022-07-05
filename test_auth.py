import pytest
import requests

import settings


# параметризация для запуска нескольких однотипных тестов
@pytest.mark.parametrize('status_code', [401, 200, ])
def test_auth_token(access_token, status_code):
    """Проверка запроса к api с требованием access_token"""
    # url для тестов, который требует access_token в запросе
    url = 'https://api.timetta.com/odata/TimeSheets?$apply=filter((userId%20eq%20e5abbd70-c398-42' \
          '76-890f-47181bd3a552)%20and%20(approvalStatus/code%20eq%20%27Draft%27)%20and%20(dueDat' \
          'e%20lt%202022-07-05))/aggregate($count%20as%20count)'
    # добавляем заголовок access_token при необходимости получения ответа 200
    headers = settings.HEADERS
    if status_code == 200:
        headers['Authorization'] = f'Bearer {access_token}'

    # отправляем get запрос и получаем ответ
    response = requests.get(url, headers=headers)
    # Печатаем в терминал полученный ответ
    print("Статус код " + str(response.status_code))

    # проверяем статус код ответа
    assert response.status_code == status_code, \
        f'Статус кода {status_code} в запросе не соответствует'

