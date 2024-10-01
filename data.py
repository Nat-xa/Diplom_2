
class Data:

    # Имя пользователя для генерации тела запросов
    USER_NAME = "Natali"
    # Текст ошибки при создании уже существующего пользователя
    TEXT_ERROR_EXISTENT_USER = "User already exists"
    # Текст ошибки при создании пользователя без одного из параметров
    TEXT_ERROR_CREATE_USER_WITHOUT_REQUIRED_FIELD = "Email, password and name are required fields"
    # Текст ошибки при авторизации с не корректным паролем или почтой
    TEXT_ERROR_FALSE_LOGIN_AND_PASSWORD = "email or password are incorrect"
    # Текст ошибки при попытке изменения данных пользователя без авторизации
    TEXT_ERROR_CHANGE_WITHOUT_AUTH = "You should be authorised"
    # Текст ошибки при попытки изменении почты на уже существующую
    TEXT_ERROR_CHANGE_USER_EMAIL_ALREADY_USE = "User with such email already exists"
    # Текст ошибки при получении заказов не авторизованным пользователем
    TEXT_ERROR_GET_USER_ORDERS_WITHOUT_AUTH = "You should be authorised"
    # ХЭШ ингредиентов
    INGREDIENT_HASH = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6f']
    # Тело для создания заказа без ингредиентов
    BODY_FOR_ORDER_WITHOUT_INGREDIENTS = {
        "ingredients": []
    }
    # Текст ошибки при создании заказа без ингредиентов
    TEXT_ERROR_CREATE_ORDER_WITHOUT_INGREDIENTS = "Ingredient ids must be provided"
    # Данные для проверки сценариев создания пользователя без одного из атрибутов
    param = 'body'
    value = [{'email': '', 'password': '1111111', 'name': 'Олег'},
             {'email': 'test12312@ya.ru', 'password': '', 'name': 'Петр'},
             {'email': 'test12312@ya.ru', 'password': '1111111', 'name': ''}]
