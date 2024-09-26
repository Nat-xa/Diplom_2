import requests

from urls import Urls


class InterfaceApi:
    @staticmethod
    def create_user(body):
        return requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER_ENDPOINT}', json=body)

    @staticmethod
    def delete_user(header):
        return requests.delete(f'{Urls.BASE_URL}{Urls.DELETE_USER_ENDPOINT}', headers=header)

    @staticmethod
    def login_user(body):
        return requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_ENDPOINT}', json=body)

    @staticmethod
    def change_user_with_auth(header, body):
        return requests.patch(f'{Urls.BASE_URL}{Urls.CHANGE_OR_GET_USER_ENDPOINT}', headers=header, json=body)

    @staticmethod
    def change_user_without_auth(body):
        return requests.patch(f'{Urls.BASE_URL}{Urls.CHANGE_OR_GET_USER_ENDPOINT}', json=body)

    @staticmethod
    def create_order_without_auth(body):
        return requests.post(f'{Urls.BASE_URL}{Urls.CREATE_ORDER_ENDPOINT}', json=body)

    @staticmethod
    def create_order_auth(header, body):
        return requests.post(f'{Urls.BASE_URL}{Urls.CREATE_ORDER_ENDPOINT}', headers=header, json=body)

    @staticmethod
    def get_user_orders_without_auth():
        return requests.get(f'{Urls.BASE_URL}{Urls.GET_USER_ORDERS_ENDPOINT}')

    @staticmethod
    def get_user_orders_with_auth(header):
        return requests.get(f'{Urls.BASE_URL}{Urls.GET_USER_ORDERS_ENDPOINT}', headers=header)
