from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class StationBase(BaseModel):
    class Config:
        orm_mode = True


class OneStation(StationBase):
    id: int
    condition: str
    date_created: datetime
    date_broken: Optional[datetime]


class CreateStation(StationBase):
    name: str


class UpdateStation(OneStation):
    pass


class StationState(StationBase):
    x: int
    y: int
    z: int


class FullStation(OneStation):
    x: str
    y: str
    z: str
