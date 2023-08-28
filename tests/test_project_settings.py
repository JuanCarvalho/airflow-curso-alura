from airflow_project.project_settings import API_KEY, BASE_URL


def test_settings():
    assert API_KEY
    assert BASE_URL
