import allure

from data import Data
from helper import Helper
from interface_api import InterfaceApi


class TestLoginEndpoint:

    @allure.title('Проверка успешной авторизации пользователя')
    def test_login_success(self):
        create_body = Helper.create_valid_user_body()
        InterfaceApi.create_user(create_body)
        login_body = Helper.get_login_body_from_create_body(create_body)
        login_response = InterfaceApi.login_user(login_body)
        headers = Helper.get_auth_token_and_create_headers(login_response)
        InterfaceApi.delete_user(headers)

        assert login_response.status_code == 200 and login_response.json()['success'] == True

    @allure.title('Проверка авторизации с не корректным email и паролем')
    def test_login_with_false_login_and_password(self):
        body = Helper.create_false_login_body()
        response = InterfaceApi.login_user(body)

        assert response.status_code == 401 and response.json()['message'] == Data.TEXT_ERROR_FALSE_LOGIN_AND_PASSWORD

    @allure.title('Проверка авторизации без email')
    def test_login_without_email(self):
        body = Helper.create_login_body_without_email()
        response = InterfaceApi.login_user(body)

        assert response.status_code == 401 and response.json()['message'] == Data.TEXT_ERROR_FALSE_LOGIN_AND_PASSWORD

    @allure.title('Проверка авторизации без пароля')
    def test_login_without_password(self):
        body = Helper.create_login_body_without_password()
        response = InterfaceApi.login_user(body)

        assert response.status_code == 401 and response.json()['message'] == Data.TEXT_ERROR_FALSE_LOGIN_AND_PASSWORD
