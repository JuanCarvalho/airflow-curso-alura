from typing import Any, Dict
from lib.api import API


class MockAPI(API):
    def whater(self, city: str, period_days: int = 7) -> Dict[str, Any]:
        # Implementação controlada de mock dos dados
        mock_data = {
            "address": city,
            "timezone": "UTC",
            "days": [
                {"datetime": "2023-08-24", "tempmax": 28.5, "tempmin": 20.9, 'temp': 25.7},
                {"datetime": "2023-08-25", "tempmax": 29.5, "tempmin": 21.9, 'temp': 25.7},
            ]
        }
        return mock_data
