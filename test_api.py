import pytest
import json
import requests

#using pytest for api testing
@pytest.fixture()
def main_url():
    return 'https://reqres.in'


def test_valid_login(main_url):
    url = main_url + '/api/login'
    data = {
        'email': 'eve.holt@reqres.in',
        'password': 'cityslicka'
    }
    response = requests.post(url, data=data)
    token1 = json.loads(response.text)
    assert response.status_code == 200, 'not matching'
    assert token1['token'] == 'QpwL5tke4Pnpja7X4'
