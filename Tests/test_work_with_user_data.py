import httpx
from jsonschema import validate
from core.contracts import CREATED_USER_SCHEME
import datetime

BASE_URL = "https://reqres.in/"
CREATE_USER = "api/users"


def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "leader",
    }
    response = httpx.post(BASE_URL + CREATE_USER, json=body, verify=False)
    assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'] .replace('T',' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response_json, CREATED_USER_SCHEME)
    assert response_json['name'] == body['name']
    assert responce.json['job'] == body['job']
    assert creation_date[0:16] == current_date[0:16]

def test_create_user_without_name():
    body = {
        "job": "leader",
    }
    response = httpx.post(BASE_URL + CREATE_USER, json=body, verify=False)
    assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'] .replace('T',' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response_json, CREATED_USER_SCHEME)
    assert responce.json['job'] == body['job']
    assert creation_date[0:16] == current_date[0:16]

def test_create_user_without_job():
        body = {
            "name": "morpheus",
        }
        response = httpx.post(BASE_URL + CREATE_USER, json=body, verify=False)
        assert response.status_code == 201

        response_json = response.json()
        creation_date = response_json['createdAt'].replace('T', ' ')
        current_date = str(datetime.datetime.now(datetime.UTC))

        validate(response_json, CREATED_USER_SCHEME)
        assert response_json['name'] == body['name']
        assert creation_date[0:16] == current_date[0:16]