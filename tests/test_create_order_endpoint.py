import allure

from data import Data
from helper import Helper
from interface_api import InterfaceApi


class TestCreateOrderEndpoint:

    @allure.title('Проверка создания заказа с ингредиентами авторизованным пользователем')
    def test_create_order_with_auth_and_ingredients(self, headers_after_login):
        body = Helper.create_body_for_order()
        response = InterfaceApi.create_order_auth(headers_after_login, body)

        assert response.status_code == 200 and response.json()['order']['number'] is not None

    @allure.title('Проверка создания заказа с ингредиентами не авторизованным пользователем')
    def test_create_order_without_auth_and_with_ingredients(self, headers_after_create):
        body = Helper.create_body_for_order()
        response = InterfaceApi.create_order_without_auth(body)

        assert response.status_code == 401

    @allure.title('Проверка создания заказа без ингредиентов авторизованным пользователем')
    def test_create_order_with_auth_and_without_ingredients(self, headers_after_login):
        body = Data.BODY_FOR_ORDER_WITHOUT_INGREDIENTS
        response = InterfaceApi.create_order_auth(headers_after_login, body)

        assert (response.status_code == 400 and response.json()['message'] ==
                Data.TEXT_ERROR_CREATE_ORDER_WITHOUT_INGREDIENTS)

    @allure.title('Проверка создания заказа без ингредиентов не авторизованным пользователем')
    def test_create_order_without_auth_and_without_ingredients(self, headers_after_create):
        body = Data.BODY_FOR_ORDER_WITHOUT_INGREDIENTS
        response = InterfaceApi.create_order_without_auth(body)

        assert (response.status_code == 400 and response.json()['message'] == Data.
                TEXT_ERROR_CREATE_ORDER_WITHOUT_INGREDIENTS)

    @allure.title('Проверка создания заказа авторизованным пользователем с не корректным хешем ингредиента')
    def test_create_order_with_false_hash(self, headers_after_login):
        body = Helper.create_body_with_false_hash_for_order()
        response = InterfaceApi.create_order_auth(headers_after_login, body)

        assert response.status_code == 500
