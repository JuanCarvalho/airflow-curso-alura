from typing import Any, Dict
from airflow_project.common_lib.api import API
from datetime import date


class MockAPI(API):
    def whater(self, city: str, period_days: int = 7) -> Dict[str, Any]:
        # Implementação controlada de mock dos dados
        date_today = date.today().strftime('%Y-%m-%d')
        mock_data = {
            "address": city,
            "timezone": "UTC",
            "days": [
                {"datetime": date_today, "tempmax": 28.5, "tempmin": 20.9, 'temp': 25.7},
                {"datetime": "2023-08-25", "tempmax": 29.5, "tempmin": 21.9, 'temp': 25.7},
            ]
        }
        return mock_data
