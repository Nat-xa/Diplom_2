import random

import allure

from data import Data


class Helper:

    @staticmethod
    @allure.title('Генерация валидного email')
    def generate_valid_email():
        return f"natali_dmitrievskyi_12_{random.randint(100, 999)}@yandex.ru"

    @staticmethod
    @allure.title('Генерация валидного пароля')
    def generate_valid_password():
        return f"F{random.randint(10, 99)}-{random.randint(10, 99)}"

    @staticmethod
    @allure.title('Создание валидного тела запроса для создания пользователя')
    def create_valid_user_body():
        email = Helper.generate_valid_email()
        password = Helper.generate_valid_password()
        body = {
            "email": email,
            "password": password,
            "name": Data.USER_NAME
        }
        return body

    @staticmethod
    @allure.title('Получение accessToken и создание заголовков с авторизацией')
    def get_auth_token_and_create_headers(response):
        user_token = response.json()['accessToken']
        headers = {'Authorization': f'{user_token}'}
        return headers

    @staticmethod
    @allure.title('Получение тела запроса для авторизации из тела запроса создания пользователя')
    def get_login_body_from_create_body(create_body):
        email = create_body['email']
        password = create_body['password']
        login_body = {
            "email": email,
            "password": password,
        }
        return login_body

    @staticmethod
    @allure.title('Создание не валидного тела запроса для авторизации')
    def create_false_login_body():
        email = Helper.generate_valid_password()
        password = Helper.generate_valid_email()
        body = {
            "email": email,
            "password": password,
        }
        return body

    @staticmethod
    @allure.title('Создание тела запроса для авторизации без email')
    def create_login_body_without_email():
        password = Helper.generate_valid_password()
        body = {
            "email": "",
            "password": password,
        }
        return body

    @staticmethod
    @allure.title('Создание тела запроса для авторизации без пароля')
    def create_login_body_without_password():
        email = Helper.generate_valid_email()
        body = {
            "email": email,
            "password": "",
        }
        return body

    @staticmethod
    @allure.title('Создание тела запроса с уже используемым email')
    def create_body_with_same_email(create_body):
        password = Helper.generate_valid_password()
        body = {
            "email": create_body['email'],
            "password": password,
            "name": Data.USER_NAME
        }
        return body

    @staticmethod
    @allure.title('Создание валидного тела запроса для оформления заказа')
    def create_body_for_order():
        body = {
            "ingredients": Data.INGREDIENT_HASH
        }
        return body

    @staticmethod
    @allure.title('Создание тела запроса для оформления заказа с не валидным хэшем')
    def create_body_with_false_hash_for_order():
        body = {
            "ingredients": f'{Data.INGREDIENT_HASH}'
        }
        return body
