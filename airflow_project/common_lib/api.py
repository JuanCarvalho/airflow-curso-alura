import requests  # type: ignore
from typing import Any, Dict
from datetime import datetime, timedelta

import airflow_project.project_settings as project_settings


class WeatherAPI:
    api_key = project_settings.WEATHER_API_KEY
    base_url = project_settings.WEATHER_BASE_URL
    api_urls = project_settings.WEATHER_API_URLS

    def _period(self, period_days: int):
        start_date = datetime.today()
        end_date = start_date + timedelta(days=period_days)
        str_start = start_date.strftime('%Y-%m-%d')
        str_end = end_date.strftime('%Y-%m-%d')
        return str_start, str_end

    def weather(self, city: str, period_days: int = 7) -> Dict[str, Any]:
        weather_url = self.api_urls['weather']
        start_date, end_date = self._period(period_days)
        url = f'{weather_url}/{city}/{start_date}/{end_date}?unitGroup=metric&include=days&key={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # type: ignore
        return {}
