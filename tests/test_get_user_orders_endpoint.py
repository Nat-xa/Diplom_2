import allure

from data import Data
from helper import Helper
from interface_api import InterfaceApi


class TestGetUserOrdersEndpoint:

    @allure.title('Проверка успешного получения списка заказов конкретного пользователя')
    def test_get_user_orders_success(self):
        create_body = Helper.create_valid_user_body()
        InterfaceApi.create_user(create_body)
        login_body = Helper.get_login_body_from_create_body(create_body)
        login_response = InterfaceApi.login_user(login_body)
        headers = Helper.get_auth_token_and_create_headers(login_response)
        body_1 = Helper.create_body_for_order()
        InterfaceApi.create_order_auth(headers, body_1)
        body_2 = Helper.create_body_for_order()
        InterfaceApi.create_order_auth(headers, body_2)
        response = InterfaceApi.get_user_orders_with_auth(headers)
        InterfaceApi.delete_user(headers)

        assert response.status_code == 200 and len(response.json()['orders']) == 2

    @allure.title('Проверка получения списка заказов неавторизованным пользователем')
    def test_get_user_orders_without_auth(self):
        response = InterfaceApi.get_user_orders_without_auth()
        assert (response.status_code == 401 and response.json()['message'] ==
                Data.TEXT_ERROR_GET_USER_ORDERS_WITHOUT_AUTH)
