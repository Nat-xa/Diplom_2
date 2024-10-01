import allure
import pytest

from helper import Helper
from interface_api import InterfaceApi


@pytest.fixture(scope='function')
@allure.title('Создание пользователя, авторизация под ним, получение заголовков с токеном, удаление пользователя '
              'после теста')
def headers_after_login():
    create_body = Helper.create_valid_user_body()
    InterfaceApi.create_user(create_body)
    login_body = Helper.get_login_body_from_create_body(create_body)
    login_response = InterfaceApi.login_user(login_body)
    headers = Helper.get_auth_token_and_create_headers(login_response)

    yield headers

    InterfaceApi.delete_user(headers)


@pytest.fixture(scope='function')
@allure.title('Создание нового пользователя и получение заголовков с токеном, удаление пользователя после теста')
def headers_after_create():
    create_body = Helper.create_valid_user_body()
    create_response = InterfaceApi.create_user(create_body)
    headers = Helper.get_auth_token_and_create_headers(create_response)

    yield headers

    InterfaceApi.delete_user(headers)
