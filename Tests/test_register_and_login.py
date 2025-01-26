import httpx
from jsonschema import validate
from core.contracts import REGISTERED_USER_SCHEME
from core.contracts import LOGIN_USER_SCHEME

BASE_URL = "https://reqres.in/"
REGISTER_USER = "api/register"
LOGIN_SUCCESSFUL_USER = "api/login"

json_file = open('/Users/ramisk/PYprojects/lesson_rvs/core/new_users_data.json')
users_data = json.load(json_file)
json_file = open('/Users/ramisk/PYprojects/lesson_rvs/core/user_login_data.json')
users_login = json.load(json_file)

@pytest.mark.parametrize('users_data' , users_data)
def test_successful_register(users_data):
    response = httpx.post(BASE_URL + REGISTER_USER, json=users_data)
    assert response.status_code == 200

    validate(response.json(), REGISTERED_USER_SCHEME)

def test_unsuccessful_register(users_data):
    response = httpx.post(BASE_URL + REGISTER_USER, json=users_data)
    assert response.status_code == 400

@pytest.mark.parametrize('users_data', users_data)
def test_login_successful(users_data):
        response = httpx.post(BASE_URL + LOGIN_SUCCESSFUL_USER, json=users_data)
        assert response.status_code == 200

        validate(response.json(), LOGIN_USER_SCHEME)