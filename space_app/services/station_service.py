import datetime
from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models
from ..database import get_session

from ..schemas.indication import IndicationBase
from ..schemas.station import StationBase, CreateStation
from .indication_service import IndicationService


class StationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, station_id: int) -> models.Station:
        station = self.session.query(models.Station).filter_by(id=station_id).first()
        if not station:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return station

    def get_all_station(self) -> List[models.Station]:
        stations = self.session.query(models.Station).all()
        return stations

    def get_one_station(self, station_id: int) -> models.Station:
        return self._get(station_id)

    def create_station(self, station_data: CreateStation) -> models.Station:
        try:
            station = models.Station(**station_data.dict())
            self.session.add(station)
            self.session.commit()
            return station
        except Exception as e:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Something wrong")

    def update_station(self, station_id: int, station_data: StationBase) -> models.Station:
        station = self._get(station_id)
        for item, value in station_data:
            setattr(station, item, value)
        try:
            self.session.commit()
            return station
        except Exception as e:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Something wrong")

    def delete_station(self, station_id: int):
        station = self._get(station_id)
        self.session.delete(station)
        self.session.commit()

    def update_coord(self, station_id: int, user_id: int, indication_data: IndicationBase) -> models.Station:
        station = self._get(station_id)
        position = indication_data.dict().get('axis')
        distance = indication_data.dict().get('distance')
        IndicationService.create_indication(self, indication_data, user_id=user_id)

        if position == 'x':
            station.x += distance
        elif position == 'y':
            station.y += distance
        else:
            station.z += distance
        if not all([item > 0 for item in (int(station.x), int(station.y), int(station.z))]):
            station.condition = 'broken'
            station.date_broken = datetime.datetime.utcnow()
        self.session.add(station)
        self.session.commit()
        return station

    def create_many_stations(self,
                             station_data: List[CreateStation]) -> List[models.Station]:
        stations = [
            models.Station(
                **item.dict(),
            )
            for item in station_data
        ]
        self.session.add_all(stations)
        self.session.commit()
        return stations


