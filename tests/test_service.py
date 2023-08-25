import pytest
from unittest.mock import patch
from datetime import date
from lib.service import Service
from tests.mock.mock_api import MockAPI


@pytest.fixture(scope="module")
def service():
    instance = Service()
    instance.api = MockAPI()
    return instance


def test_whater(service: Service):
    response = service.whater('Buenos Aires')
    assert response['address'] == 'Buenos Aires'
    str_today = date.today().strftime('%Y-%m-%d')
    assert response['days'][0]['datetime'] == str_today
