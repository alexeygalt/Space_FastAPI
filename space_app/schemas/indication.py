from enum import Enum

from pydantic import BaseModel


class AxisKind(str, Enum):
    x = 'x'
    y = 'y'
    z = 'z'


class IndicationBase(BaseModel):
    axis: AxisKind
    distance: int

    class Config:
        orm_mode = True


class OneIndication(IndicationBase):
    id: int
    user : str


class CreateIndication(IndicationBase):
   pass
