from pydantic import BaseModel
from typing import List


class Days(BaseModel):
    datetime: str
    tempmax: float
    tempmin: float
    temp: float


class Whater(BaseModel):
    address: str
    timezone: str
    days: List[Days]
