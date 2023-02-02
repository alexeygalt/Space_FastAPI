import fastapi
import pytest

from space_app import models
from space_app.models import Station
from space_app.schemas.indication import IndicationBase
from space_app.schemas.station import CreateStation
from space_app.services.station_service import StationService


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


class TestStationService:

    @pytest.fixture
    def stations_session(self, session):
        return StationService(session)

    @pytest.fixture
    def station_1(self, session):
        s = Station(name='test_1')
        session.add(s)
        session.commit()
        return s

    @pytest.fixture
    def station_2(self, session):
        s = Station(name='test_2')
        session.add(s)
        session.commit()
        return s

    def test_get_one_station(self, station_1, stations_session):
        assert stations_session._get(station_1.id) == station_1

    def test_get_all_station(self, station_1, station_2, stations_session):
        assert stations_session.get_all_station() == [station_1, station_2]

    def test_create(self, stations_session, station_2):
        data = CreateStation(name='Test')
        new_station = stations_session.create_station(data)

        assert new_station.id == 2
        assert new_station.name == "Test"

    def test_update_station(self, stations_session, station_2, station_id=1):
        data = CreateStation(name='updated')
        updated_station = stations_session.update_station(station_id, data)
        assert station_2.name == 'updated'

    def test_delete_station(self, station_1, stations_session):
        stations_session.delete_station(station_1.id)
        with pytest.raises(fastapi.exceptions.HTTPException):
            stations_session.get_one_station(station_1.id)

    def test_create_many_stations(self, stations_session):
        data = [CreateStation(name='test_1'), CreateStation(name='test_2')]
        stations_session.create_many_stations(data)
        assert len(stations_session.get_all_station()) == 2

    def test_update_coords_1(self, stations_session, station_1, user_token):
        data = IndicationBase(axis='x', distance=300)
        station = stations_session.update_coord(station_id=station_1.id, user_id=user_token.id,
                                            indication_data=data)
        assert station.x == 400
        assert station.condition == "running"

    def test_update_coords_2(self, stations_session, station_1, user_token):
        data = IndicationBase(axis='y', distance=300)
        updated_station = stations_session.update_coord(station_id=station_1.id, user_id=user_token.id,
                                                        indication_data=data)
        assert updated_station.y == 400
        assert updated_station.condition == "running"

    def test_update_coords_3(self, stations_session, station_1, user_token):
        data = IndicationBase(axis='z', distance=300)
        updated_station = stations_session.update_coord(station_id=station_1.id, user_id=user_token.id,
                                                        indication_data=data)
        assert updated_station.z == 400
        assert updated_station.condition == "running"

    def test_update_coords_4(self, stations_session, station_1, user_token):
        data = IndicationBase(axis='x', distance=-200)
        updated_station = stations_session.update_coord(station_id=station_1.id, user_id=user_token.id,
                                                        indication_data=data)
        assert updated_station.condition == "broken"
        assert updated_station.date_broken is not None

    def test_update_coords_5(self, stations_session, station_1, user_token):
        data = IndicationBase(axis='y', distance=-200)
        updated_station = stations_session.update_coord(station_id=station_1.id, user_id=user_token.id,
                                                        indication_data=data)
        assert updated_station.condition == "broken"
        assert updated_station.date_broken is not None

    def test_update_coords_6(self, stations_session, station_1, user_token):
        data = IndicationBase(axis='z', distance=-200)
        updated_station = stations_session.update_coord(station_id=station_1.id, user_id=user_token.id,
                                                        indication_data=data)
        assert updated_station.condition == "broken"
        assert updated_station.date_broken is not None