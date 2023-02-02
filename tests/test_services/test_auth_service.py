import pytest

from space_app.models import User
from space_app.schemas.auth import UserCreate
from space_app.services.auth_service import AuthService


class TestAuthService:

    @pytest.fixture
    def auth_session(self, session):
        return AuthService(session)

    @pytest.fixture
    def user_1(self, session, auth_session):
        s = User(email='test', username='test', password_hash=auth_session.hash_password('test'))
        session.add(s)
        session.commit()
        return s

    def test_register_new_user(self, auth_session):
        data = UserCreate(email='test', username='test', password='test')
        token = auth_session.register_new_user(data)
        assert token.access_token is not None
        assert token.token_type == 'bearer'

    def test_authenticate_user(self, auth_session, user_1):
        token = auth_session.authenticate_user(username='test', password='test')
        assert token.access_token is not None
        assert token.token_type == 'bearer'

    def test_user_page(self, client, auth_session):
        data = UserCreate(email='test', username='test', password='test')
        token = auth_session.register_new_user(data)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token.access_token}'
        }
        response = client.get('/auth/user', headers=headers)

        assert response.status_code == 200
