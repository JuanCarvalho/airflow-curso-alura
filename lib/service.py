from typing import Any, Dict

from lib.api import API
from lib.serializers import Whater
from lib.utils import set_serializer


class Service:
    api = API()

    @set_serializer(Whater)
    def whater(self, city: str, period_days: int = 7) -> Dict[str, Any]:
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
        return whater_data
