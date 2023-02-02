import json

import pytest

from space_app.schemas.station import CreateStation
from space_app.services.station_service import StationService


@pytest.fixture
def stations_session(session):
    return StationService(session)


def test_get_empty_stations_list(client):
    response = client.get('/stations')

    assert response.status_code == 200
    assert response.json() == []


def test_create_station(client, stations_session):
    data = {"name": "test"}

    response = client.post('/stations/', data=json.dumps(data))

    assert response.status_code == 200


def test_create_station_unique_name(client, stations_session):
    station = CreateStation(name='test')
    stations_session.create_station(station)
    data = {'name': 'test'}
    response = client.post('/stations/', data=json.dumps(data))
    assert response.status_code == 400


def test_update_station(client, stations_session):
    station_data = CreateStation(name='test')
    station = stations_session.create_station(station_data)
    data = {'name': 'updated'}
    response = client.put('/stations/1/', data=json.dumps(data))
    assert response.status_code == 200
    assert station.name == 'updated'


def test_delete_station(client, stations_session):
    station_data = CreateStation(name='test')
    stations_session.create_station(station_data)
    response = client.delete('/stations/1/')
    assert response.status_code == 204


def test_station_not_found(client):
    response = client.get('/stations/1')

    assert response.status_code == 404
