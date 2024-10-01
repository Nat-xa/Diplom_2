import allure
import requests

from urls import Urls


class InterfaceApi:
    @staticmethod
    @allure.title('Запрос для создания пользователя')
    def create_user(body):
        return requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER_ENDPOINT}', json=body)

    @staticmethod
    @allure.title('Запрос для удаления пользователя')
    def delete_user(header):
        return requests.delete(f'{Urls.BASE_URL}{Urls.DELETE_USER_ENDPOINT}', headers=header)

    @staticmethod
    @allure.title('Запрос для авторизации пользователя')
    def login_user(body):
        return requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_ENDPOINT}', json=body)

    @staticmethod
    @allure.title('Запрос для изменения данных авторизованного пользователя')
    def change_user_with_auth(header, body):
        return requests.patch(f'{Urls.BASE_URL}{Urls.CHANGE_OR_GET_USER_ENDPOINT}', headers=header, json=body)

    @staticmethod
    @allure.title('Запрос для изменения данных не авторизованного пользователя')
    def change_user_without_auth(body):
        return requests.patch(f'{Urls.BASE_URL}{Urls.CHANGE_OR_GET_USER_ENDPOINT}', json=body)

    @staticmethod
    @allure.title('Запрос для создания заказа не авторизованным пользователем')
    def create_order_without_auth(body):
        return requests.post(f'{Urls.BASE_URL}{Urls.CREATE_ORDER_ENDPOINT}', json=body)

    @staticmethod
    @allure.title('Запрос для создания заказа авторизованным пользователем')
    def create_order_auth(header, body):
        return requests.post(f'{Urls.BASE_URL}{Urls.CREATE_ORDER_ENDPOINT}', headers=header, json=body)

    @staticmethod
    @allure.title('Запрос для получения списка заказов пользователем без авторизации')
    def get_user_orders_without_auth():
        return requests.get(f'{Urls.BASE_URL}{Urls.GET_USER_ORDERS_ENDPOINT}')

    @staticmethod
    @allure.title('Запрос для получения списка заказов авторизованным пользователем')
    def get_user_orders_with_auth(header):
        return requests.get(f'{Urls.BASE_URL}{Urls.GET_USER_ORDERS_ENDPOINT}', headers=header)
