import pytest

from space_app import models


@pytest.fixture
def user_token(client, session):
    data = {
        "username": 'user',
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
        {"username": data['username'], "password": data['password_hash']},
        format="json"
    )
    return response.data['access']
