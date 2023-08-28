from typing import Any, Dict, List
from airflow_project.common_lib.api import API
from airflow_project.common_lib.serializers import TemperatureModel
from airflow_project.common_lib.utils import method_serializer


class APIService:
    api = API()

    @method_serializer(TemperatureModel)
    def whater(self, city: str, period_days: int = 7) -> List[Dict[str, Any]]:
        """
        ### Return the weather forecast for the next 7 days

        ##### Params:
        :param city: City name
        :param period_days: Number of days to forecast

        :return: Dict[str, Any]

        ##### Usage:
        ```python
        instance = Service()
        instance.whater('São Paulo', 2)
        ```
        """
        whater_data = self.api.whater(city, period_days)
        list_days: List[Dict[str, Any]] = whater_data['days']
        return list_days
