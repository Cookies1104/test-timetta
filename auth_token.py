import requests

import settings


class AuthToken:
    _instance = None  # для реализации Singleton

    def __new__(cls, *args, **kwargs):
        """Реализация Singleton. Используем для исключения повторных обращений за обновлением
        токенов"""
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        """Инициализация и получение токенов"""
        # Создаём переменные токенов
        self.__access_token: str | None = None
        self.__refresh_token: str | None = None
        # Запрашиваем токены в 1 раз
        self.get_access_and_refresh_tokens()

    def get_access_and_refresh_tokens(self) -> None:
        """Получаем токены по логину и паролю"""
        # тело запроса
        body = {
            'client_id': 'external',
            'scope': 'all offline_access',
            'grant_type': 'password',
            'username': settings.LOGIN,
            'password': settings.PASSWORD,
        }
        # отправляем запрос на сервер авторизации и получаем ответ
        response = requests.post(url=settings.AUTH_URL,
                                 headers=settings.HEADERS,
                                 data=body)
        # обновляем переменные токенов
        self.__refresh_token = response.json()['refresh_token']
        self.__access_token = response.json()['access_token']

    def update_tokens(self) -> None:
        """Обновляем токены по refresh_token в случае истечения времени access_token"""
        # если refresh_token не существует отправляем запрос на получение по логину и паролю
        if not self.__refresh_token:
            self.get_access_and_refresh_tokens()
            return None

        # тело запроса
        body = {
            'client_id': 'external',
            'scope': 'all offline_access',
            'grant_type': 'refresh_token',
            'refresh_token': self.__refresh_token,
        }
        # отправляем запрос на сервер авторизации и получаем ответ
        response = requests.post(url=settings.AUTH_URL,
                                 headers=settings.HEADERS,
                                 data=body)
        # обновляем переменные токенов
        self.__refresh_token = response.json()['refresh_token']
        self.__access_token = response.json()['access_token']

    @property
    def access_token(self) -> str:
        """Get access_token"""
        return self.__access_token

    @property
    def refresh_token(self) -> str:
        """Get refresh_token"""
        return self.__refresh_token
