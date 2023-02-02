from fastapi import APIRouter, Depends

from space_app.schemas.auth import User
from space_app.schemas.indication import IndicationBase
from space_app.schemas.station import StationState
from space_app.services.auth_service import get_current_user
from space_app.services.station_service import StationService

router = APIRouter(
    prefix='/stations/{station_id}/state',
    tags=['Change Coords']
)


@router.get('/', response_model=StationState)
def get_station_state(station_id: int,
                      service: StationService = Depends()):
    """
    Get station's Position
    \f
    :param station_id:
    :param service:
    :return:
    """
    return service.get_one_station(station_id)


@router.post('/', response_model=StationState)
def update_station_coords(station_id: int,
                          indication_data: IndicationBase,
                          service: StationService = Depends(),
                          user: User = Depends(get_current_user)):
    """
    Set new station's Position
    \f
    :param station_id:
    :param indication_data:
    :param service:
    :param user:
    :return:
    """
    return service.update_coord(station_id=station_id, indication_data=indication_data, user_id=user.id)
