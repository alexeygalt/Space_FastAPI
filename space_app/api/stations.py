from typing import List

from fastapi import APIRouter, Depends, Response, status

from space_app.schemas.station import OneStation, CreateStation
from space_app.services.station_service import StationService

router = APIRouter(
    prefix='/stations',
    tags=['Stations']
)


@router.get('/', response_model=List[OneStation])
def get_stations(service: StationService = Depends()):
    """
    Show all Stations
    \f
    :param service:
    :return:
    """
    return service.get_all_station()


@router.get('/{station_id}', response_model=OneStation)
def get_one_station(station_id: int,
                    service: StationService = Depends()):
    """
    Retrieve Station
    \f
    :param station_id:
    :param service:
    :return:
    """
    return service.get_one_station(station_id)


@router.post('/', response_model=OneStation)
def create_station(station_data: CreateStation,
                   service: StationService = Depends()):
    """
    Create new Station
    \f
    :param station_data:
    :param service:
    :return:
    """
    return service.create_station(station_data)


@router.put('/{station_id}', response_model=OneStation)
def update_station(station_id: int,
                   station_data: CreateStation,
                   service: StationService = Depends()):
    """
    Update station's Name
    \f
    :param station_id:
    :param station_data:
    :param service:
    :return:
    """
    return service.update_station(station_id, station_data)


@router.delete('/{station_id}')
def delete_station(station_id: int,
                   service: StationService = Depends()):
    """
    Delete Station
    \f
    :param station_id:
    :param service:
    :return:
    """
    service.delete_station(station_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
