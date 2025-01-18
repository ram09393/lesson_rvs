import httpx
from jsonschema import validate
from Schema.Schema_Resource import LIST_RESOURCE_SCHEME

BASE_URL = "https://reqres.in/"
LIST_RESOURCE = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
NOT_FOUND_RESOURCE = "api/unknown/23"
Color_Symbol = "#"

def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE, verify=False)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, LIST_RESOURCE_SCHEME)
        assert str(item['color']).startswith(Color_Symbol)

def test_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE, verify=False)
    assert response.status_code == 200
    data = response.json()['data']
    assert str(data['color']).startswith(Color_Symbol)

def test_single_resource_not_found():
    response = httpx.get(BASE_URL + NOT_FOUND_RESOURCE, verify=False)
    assert response.status_code == 404