import os

from dotenv import load_dotenv

# загружаем переменные из виртуального окружения и файла .env
load_dotenv()
# получаем переменную логина из вирт.окр.
LOGIN = os.getenv('LOGIN')
# получаем переменную пароля из вирт.окр.
PASSWORD = os.getenv('PASSWORD')
# глобальная переменная url адреса для получения/обновления токенов
AUTH_URL = 'https://auth.timetta.com/connect/token'
# глобальная переменная заголовков для получения/обновления токенов
HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}

