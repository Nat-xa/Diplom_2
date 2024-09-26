import allure

from data import Data
from helper import Helper
from interface_api import InterfaceApi


class TestCreateOrderEndpoint:

    @allure.title('Проверка создания заказа с ингредиентами авторизованным пользователем')
    def test_create_order_with_auth_and_ingredients(self):
        create_body = Helper.create_valid_user_body()
        InterfaceApi.create_user(create_body)
        login_body = Helper.get_login_body_from_create_body(create_body)
        login_response = InterfaceApi.login_user(login_body)
        headers = Helper.get_auth_token_and_create_headers(login_response)
        body = Helper.create_body_for_order()
        response = InterfaceApi.create_order_auth(headers, body)
        InterfaceApi.delete_user(headers)

        assert response.status_code == 200 and response.json()['order']['number'] is not None

    @allure.title('Проверка создания заказа с ингредиентами не авторизованным пользователем')
    def test_create_order_without_auth_and_with_ingredients(self):
        create_body = Helper.create_valid_user_body()
        InterfaceApi.create_user(create_body)
        login_body = Helper.get_login_body_from_create_body(create_body)
        login_response = InterfaceApi.login_user(login_body)
        headers = Helper.get_auth_token_and_create_headers(login_response)
        body = Helper.create_body_for_order()
        response = InterfaceApi.create_order_without_auth(body)
        InterfaceApi.delete_user(headers)

        assert response.status_code == 401

    @allure.title('Проверка создания заказа без ингредиентов авторизованным пользователем')
    def test_create_order_with_auth_and_without_ingredients(self):
        create_body = Helper.create_valid_user_body()
        InterfaceApi.create_user(create_body)
        login_body = Helper.get_login_body_from_create_body(create_body)
        login_response = InterfaceApi.login_user(login_body)
        headers = Helper.get_auth_token_and_create_headers(login_response)
        body = Data.BODY_FOR_ORDER_WITHOUT_INGREDIENTS
        response = InterfaceApi.create_order_auth(headers, body)
        InterfaceApi.delete_user(headers)

        assert (response.status_code == 400 and response.json()['message'] ==
                Data.TEXT_ERROR_CREATE_ORDER_WITHOUT_INGREDIENTS)

    @allure.title('Проверка создания заказа без ингредиентов не авторизованным пользователем')
    def test_create_order_without_auth_and_without_ingredients(self):
        create_body = Helper.create_valid_user_body()
        InterfaceApi.create_user(create_body)
        login_body = Helper.get_login_body_from_create_body(create_body)
        login_response = InterfaceApi.login_user(login_body)
        headers = Helper.get_auth_token_and_create_headers(login_response)
        body = Data.BODY_FOR_ORDER_WITHOUT_INGREDIENTS
        response = InterfaceApi.create_order_without_auth(body)
        InterfaceApi.delete_user(headers)

        assert (response.status_code == 400 and response.json()['message'] == Data.
                TEXT_ERROR_CREATE_ORDER_WITHOUT_INGREDIENTS)

    @allure.title('Проверка создания заказа авторизованным пользователем с не корректным хешем ингредиента')
    def test_create_order_with_false_hash(self):
        create_body = Helper.create_valid_user_body()
        InterfaceApi.create_user(create_body)
        login_body = Helper.get_login_body_from_create_body(create_body)
        login_response = InterfaceApi.login_user(login_body)
        headers = Helper.get_auth_token_and_create_headers(login_response)
        body = Helper.create_body_with_false_hash_for_order()
        response = InterfaceApi.create_order_auth(headers, body)
        InterfaceApi.delete_user(headers)

        assert response.status_code == 500
