import httpx
from jsonschema import validate
from Schema.Schema_Resource import LIST_RESOURCE_SCHEME
import allure

BASE_URL = "https://reqres.in/"
LIST_RESOURCE = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
NOT_FOUND_RESOURCE = "api/unknown/23"
Color_Symbol = "#"

@allure.suite('Проверка запросов ресурсов')
@allure.title('Проверяем получение списка ресурсов')

def test_list_resource():
    with allure.step(f'Делаем запрос по адресу:({BASE_URL + LIST_RESOURCE}'):
        response = httpx.get(BASE_URL + LIST_RESOURCE, verify=False)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']
    for item in data:
        with allure.step('Проверяем шаги'):
            validate(item, LIST_RESOURCE_SCHEME)
        with allure.step('Проверяем наличие # в коде цвета'):
            assert str(item['color']).startswith(Color_Symbol)

def test_single_resource():
    with allure.step(f'Делаем запрос по адресу:({BASE_URL + SINGLE_RESOURCE}'):
        response = httpx.get(BASE_URL + SINGLE_RESOURCE, verify=False)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']
    with allure.step('Проверяем наличие # в коде цвета'):
        assert str(data['color']).startswith(Color_Symbol)

def test_single_resource_not_found():
    with allure.step(f'Делаем запрос по адресу:({BASE_URL + NOT_FOUND_RESOURCE}'):
        response = httpx.get(BASE_URL + NOT_FOUND_RESOURCE, verify=False)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404