import pytest
from datetime import date
from airflow_project.common_lib.service import APIService
from tests.mock.mock_api import MockAPI


@pytest.fixture(scope="module")
def service():
    instance = APIService()
    instance.api = MockAPI()
    return instance


def test_whater(service: APIService):
    response = service.whater('Buenos Aires')
    str_today = date.today().strftime('%Y-%m-%d')
    assert response[0]['datetime'] == str_today
