from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session


from .. import models
from ..database import get_session
from ..schemas.indication import IndicationBase


class IndicationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, indication_id: int) -> models.Indication:
        indication = self.session.query(models.Indication).filter_by(id=indication_id).first()
        if not indication:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return indication

    def get_one_indication(self, indication_id: int) -> models.Indication:
        return self._get(indication_id)

    def get_list_indications(self) -> List[models.Indication]:
        indications = self.session.query(models.Indication).all()
        return indications

    def create_indication(self, indication_data: IndicationBase,
                          user_id: int, ) -> models.Indication:
        try:
            indication = models.Indication(**indication_data.dict())
            indication.user_id = user_id
            user = self.session.query(models.User).filter_by(id=user_id).first()
            indication.user = user.username
            self.session.add(indication)
            self.session.commit()
            return indication
        except Exception as e:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Something wrong")
