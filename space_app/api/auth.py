from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from space_app.schemas.auth import Token, UserCreate, User
from space_app.services.auth_service import AuthService, get_current_user

router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)


@router.post('/sing-up', response_model=Token)
def sing_up(user_data: UserCreate, service: AuthService = Depends()):
    """
    Register new User
    \f
    :param user_data:
    :param service:
    :return:
    """
    return service.register_new_user(user_data)


@router.post('/sign-in', response_model=Token)
def sing_in(form_data: OAuth2PasswordRequestForm = Depends(),
            service: AuthService = Depends()):
    """
    Log in
    \f
    :param form_data:
    :param service:
    :return:
    """
    return service.authenticate_user(
        form_data.username,
        form_data.password
    )


@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    """
    Get user's Info
    \f
    :param user:
    :return:
    """
    return user
