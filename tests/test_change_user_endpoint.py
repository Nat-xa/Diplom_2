import allure

from data import Data
from helper import Helper
from interface_api import InterfaceApi


class TestChangeUserEndpoint:

    @allure.title('Проверка успешного изменения данных пользователя')
    def test_change_user_success(self):
        create_body = Helper.create_valid_user_body()
        InterfaceApi.create_user(create_body)
        login_body = Helper.get_login_body_from_create_body(create_body)
        login_response = InterfaceApi.login_user(login_body)
        headers = Helper.get_auth_token_and_create_headers(login_response)
        change_body = Helper.create_valid_user_body()
        response = InterfaceApi.change_user_with_auth(headers, change_body)
        InterfaceApi.delete_user(headers)

        assert (response.status_code == 200 and response.json()['user']['name'] == change_body['name'] and
                response.json()['user']['email'] == change_body['email'])

    @allure.title('Проверка изменения данных пользователя на email, который уже используется')
    def test_change_user_email_already_use(self):
        create_body_1 = Helper.create_valid_user_body()
        InterfaceApi.create_user(create_body_1)
        create_body_2 = Helper.create_valid_user_body()
        create_response_2 = InterfaceApi.create_user(create_body_2)
        headers_2 = Helper.get_auth_token_and_create_headers(create_response_2)
        login_body = Helper.get_login_body_from_create_body(create_body_1)
        login_response = InterfaceApi.login_user(login_body)
        headers_1 = Helper.get_auth_token_and_create_headers(login_response)
        change_body = Helper.create_body_with_same_email(create_body_2)
        response = InterfaceApi.change_user_with_auth(headers_1, change_body)
        InterfaceApi.delete_user(headers_1)
        InterfaceApi.delete_user(headers_2)

        assert (response.status_code == 403 and response.json()['message'] ==
                Data.TEXT_ERROR_CHANGE_USER_EMAIL_ALREADY_USE)

    @allure.title('Проверка изменения данных не авторизованного пользователя')
    def test_change_user_without_auth(self):
        create_body = Helper.create_valid_user_body()
        create_response = InterfaceApi.create_user(create_body)
        headers = Helper.get_auth_token_and_create_headers(create_response)
        change_body = Helper.create_valid_user_body()
        response = InterfaceApi.change_user_without_auth(change_body)
        InterfaceApi.delete_user(headers)

        assert response.status_code == 401 and response.json()['message'] == Data.TEXT_ERROR_CHANGE_WITHOUT_AUTH
