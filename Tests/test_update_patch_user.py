import httpx
from jsonschema import validate
from core.contracts import UPDATE_USER_SCHEME
import datetime

BASE_URL = "https://reqres.in/"
UPDATE_USER = "api/users/2"


def test_update_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "zion resident",
    }
    response = httpx.patch(BASE_URL + UPDATE_USER, json=body, verify=False)
    assert response.status_code == 200

    response_json = response.json()
    creation_date = response_json['updatedAt'] .replace('T',' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response_json, UPDATE_USER_SCHEME)
    assert response_json['name'] == body['name']
    assert responce.json['job'] == body['job']
    assert creation_date[0:16] == current_date[0:16]

def test_update_user_without_name():
    body = {
        "job": "leader",
    }
    response = httpx.patch(BASE_URL + UPDATE_USER, json=body, verify=False)
    assert response.status_code == 200

    response_json = response.json()
    creation_date = response_json['updatedAt'] .replace('T',' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response_json, UPDATE_USER_SCHEME)
    assert responce.json['job'] == body['job']
    assert creation_date[0:16] == current_date[0:16]

def test_update_user_without_job():
        body = {
            "name": "morpheus",
        }
        response = httpx.patch(BASE_URL + UPDATE_USER, json=body, verify=False)
        assert response.status_code == 200

        response_json = response.json()
        creation_date = response_json['updatedAt'].replace('T', ' ')
        current_date = str(datetime.datetime.now(datetime.UTC))

        validate(response_json, UPDATE_USER_SCHEME)
        assert response_json['name'] == body['name']
        assert creation_date[0:16] == current_date[0:16]