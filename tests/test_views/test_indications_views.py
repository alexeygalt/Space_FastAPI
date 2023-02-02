import pytest

from space_app import models
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


@pytest.fixture
def indications_session(session):
    return IndicationService(session)


def test_get_empty_indications_list(client):
    response = client.get('/indications')

    assert response.status_code == 200
    assert response.json() == []


def test_one_indication(client, indications_session, user_token):
    data = IndicationBase(axis='x', distance=300)
    indications_session.create_indication(data, user_id=1)
    response = client.get('/indications/1')
    expected_response = {

        "axis": "x",
        "distance": 300,
        "id": 1,
        "user": "user_1"

    }
    assert response.status_code == 200
    assert response.json() == expected_response


def test_empty_indication(client):
    response = client.get('/indications/1')
    data = {
        "detail": "Item not found"
    }
    assert response.status_code == 404
    assert response.json() == data






