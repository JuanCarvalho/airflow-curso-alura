from typing import Any, Dict, List
from airflow_project.common_lib.api import TwitterAPI, WeatherAPI
from airflow_project.common_lib.serializers import TemperatureModel, TwitterModel
from airflow_project.common_lib.utils import method_serializer


class APIService:
    api = WeatherAPI()

    @method_serializer(TemperatureModel)
    def weather(self, city: str, period_days: int = 7) -> List[Dict[str, Any]]:
        """
        ### Return the weather forecast for the next 7 days

        ##### Params:
        :param city: City name
        :param period_days: Number of days to forecast

        :return: Dict[str, Any]

        ##### Usage:
        ```python
        instance = Service()
        instance.weather('São Paulo', 2)
        ```
        """
        weather_data = self.api.weather(city, period_days)
        days: List[Dict[str, Any]] = weather_data['days']
        return days

    @method_serializer(TwitterModel)
    def twitter(self):
        """
        ### Return the twitter data

        :return: Dict[str, Any]

        ##### Usage:
        ```python
        instance = Service()
        instance.twitter()
        ```
        """
        api = TwitterAPI()
        twittes: List[Dict[str, Any]] = api.get_twitts()['data']
        return twittes
