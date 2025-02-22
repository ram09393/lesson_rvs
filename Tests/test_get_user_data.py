import httpx
from jsonschema import validate
from Schema.contracts import USER_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"
SINGLE_USER = "api/users/2"
NOT_FOUND_USER = "api/users/23"
EMAIL_ENDS = "@reqres.in"
AVATAR_ENDS = "-image.jpg"
@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение списка пользователей')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу:({BASE_URL + LIST_USERS}'):
        response = httpx.get(BASE_URL + LIST_USERS, verify=False)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step('Проверяем элемент из списка'):
            validate(item, USER_DATA_SCHEME)


with allure.step('Проверяем окончание Email адреса'):
    assert (item['email']).endswith(EMAIL_ENDS)
with allure.step('Проверяем наличие id в ссылке на аватарку'):
    assert item['avatar']. endswith(str(item['id']) + AVATAR_ENDS)
def test_single_users():
    with allure.step(f'Делаем запрос по адресу:({BASE_URL + SINGLE_USER}'):
        response = httpx.get(BASE_URL + SINGLE_USER, verify=False)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']
    with allure.step('Проверяем окончание Email адреса'):
        assert (data['email']).endswith(EMAIL_ENDS)
    with allure.step('Проверяем наличие id в ссылке на аватарку'):
        assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

def test_user_not_found():
    with allure.step(f'Делаем запрос по адресу:({BASE_URL + NOT_FOUND_USER}'):
        response = httpx.get(BASE_URL + NOT_FOUND_USER, verify=False)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404