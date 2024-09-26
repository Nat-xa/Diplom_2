import allure
import pytest

from data import Data
from helper import Helper
from interface_api import InterfaceApi


class TestCreateUserEndpoint:
    @allure.title('Проверка успешного создания пользователя')
    def test_create_new_user_success(self):
        body = Helper.create_valid_user_body()
        response = InterfaceApi.create_user(body)
        headers = Helper.get_auth_token_and_create_headers(response)
        delete_new_user = InterfaceApi.delete_user(headers)

        assert (response.status_code == 200 and response.json()['user']['name'] == Data.USER_NAME and
                delete_new_user.status_code == 202)

    @allure.title('Проверка создания уже существующего пользователя')
    def test_create_existent_user(self):
        body = Helper.create_valid_user_body()
        response_1 = InterfaceApi.create_user(body)
        response_2 = InterfaceApi.create_user(body)
        headers = Helper.get_auth_token_and_create_headers(response_1)
        InterfaceApi.delete_user(headers)

        assert response_2.status_code == 403 and response_2.json()['message'] == Data.TEXT_ERROR_EXISTENT_USER

    @pytest.mark.parametrize(Data.param, Data.value)
    @allure.title('Проверка создания пользователя без заполнения обязательных полей (email, пароль, name)')
    def test_create_user_without_param(self, body):
        response = InterfaceApi.create_user(body)

        assert (response.status_code == 403 and response.json()['message'] ==
                Data.TEXT_ERROR_CREATE_USER_WITHOUT_REQUIRED_FIELD)
