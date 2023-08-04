import datetime

from pydantic import BaseModel


class Temperature(BaseModel):
    temperature_value: int
    timestamp: datetime.datetime
