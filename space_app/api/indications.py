from typing import List

from fastapi import APIRouter, Depends

from space_app.schemas.indication import OneIndication
from space_app.services.indication_service import IndicationService

router = APIRouter(
    prefix='/indications',
    tags=['Indication']
)


@router.get('/', response_model=List[OneIndication])
def get_all_indications(service: IndicationService = Depends()):
    """
    Show all Indications
    \f
    :param service:
    :return:
    """
    return service.get_list_indications()


@router.get('/{indication_id}', response_model=OneIndication)
def get_one_indication(indication_id: int, service: IndicationService = Depends()):
    """
    Retrieve Indication
    \f
    :param indication_id:
    :param service:
    :return:
    """
    return service.get_one_indication(indication_id)

