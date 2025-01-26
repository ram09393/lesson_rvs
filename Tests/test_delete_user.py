import httpx
from jsonschema import validate

BASE_URL = "https://reqres.in/"
DELETE_USER = "api/users/2"

def test_delete_user():
    response = httpx.delete(BASE_URL + DELETE_USER, verify=False)
    assert response.status_code == 204
