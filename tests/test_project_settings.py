from airflow_project.project_settings import WEATHER_API_KEY, WEATHER_BASE_URL, BASE_PATH


def test_settings():
    assert WEATHER_API_KEY
    assert WEATHER_BASE_URL
    assert BASE_PATH
