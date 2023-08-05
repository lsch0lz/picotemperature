import datetime

from pydantic import BaseModel


class Temperature(BaseModel):
    id: str
    status: str
