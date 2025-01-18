import httpx
from jsonschema import validate
from Schema.contracts import USER_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"
SINGLE_USER = "api/users/2"
NOT_FOUND_USER = "api/users/23"
EMAIL_ENDS = "@reqres.in"
AVATAR_ENDS = "-image.jpg"

def test_list_users():
    response = httpx.get(BASE_URL + LIST_USERS, verify=False)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, USER_DATA_SCHEME)
        assert (item['email']).endswith(EMAIL_ENDS)
        assert item['avatar']. endswith(str(item['id']) + AVATAR_ENDS)

def test_single_users():
    response = httpx.get(BASE_URL + SINGLE_USER, verify=False)
    assert response.status_code == 200
    data = response.json()['data']
    assert (data['email']).endswith(EMAIL_ENDS)
    assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

def test_user_not_found():
    response = httpx.get(BASE_URL + NOT_FOUND_USER, verify=False)
    assert response.status_code == 404