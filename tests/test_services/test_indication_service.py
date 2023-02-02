import pytest
from space_app import models
from space_app.models import Indication

from space_app.schemas.indication import IndicationBase
from space_app.services.indication_service import IndicationService


@pytest.fixture
def user_token(client, session):
    data = {
        "username": 'user_1',
        "password": 'password',
        "email": "test"
    }

    user = models.User(
        email=data['email'],
        username=data['username'],
        password_hash=data['password']
    )
    session.add(user)
    session.commit()
    response = client.post(
        "/sing-up/",
        json={"username": data['username'], "password": data['password']}

    )
    return user


class TestIndicationService:

    @pytest.fixture
    def indications_session(self, session):
        return IndicationService(session)

    @pytest.fixture
    def indication_1(self, session):
        s = Indication(user='test', axis='z', distance=100, user_id=1)
        session.add(s)
        session.commit()
        return s

    @pytest.fixture
    def indication_2(self, session):
        s = Indication(user='test', axis='z', distance=100, user_id=1)
        session.add(s)
        session.commit()
        return s

    def test_get_one_indication(self, indication_1, indications_session):
        assert indications_session._get(indication_1.id) == indication_1

    def test_get_list_indications(self, indication_1, indication_2, indications_session):
        assert indications_session.get_list_indications() == [indication_1, indication_2]

    def test_create(self, indications_session, indication_2, user_token):
        data = IndicationBase(axis='x', distance=300)

        new_indication = indications_session.create_indication(data, user_token.id, )

        assert new_indication.id == 2



