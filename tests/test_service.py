import pytest
from lib.service import Service
from datetime import date


@pytest.fixture(scope="module")
def service():
    return Service()


def test_whater(service: Service):
    response = service.whater('Buenos Aires')
    assert response['address'] == 'Buenos Aires'
    str_today = date.today().strftime('%Y-%m-%d')
    assert response['days'][0]['datetime'] == str_today
