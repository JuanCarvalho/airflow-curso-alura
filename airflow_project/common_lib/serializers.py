from pydantic import BaseModel


class TemperatureModel(BaseModel):
    datetime: str
    tempmax: float
    tempmin: float
    temp: float
