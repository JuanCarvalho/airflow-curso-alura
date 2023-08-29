import pytest
from airflow_project.common_lib.api import WeatherAPI


@pytest.fixture(scope="module")
def api():
    return WeatherAPI()


def test_whater(api: WeatherAPI):
    assert api.weather('São Paulo')
