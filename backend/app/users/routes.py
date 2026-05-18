from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.users.dtos import UserRegister
from app.users.dtos import UserLogin
from app.users.dtos import UserResponse
from app.users.dtos import TokenResponse

from app.users.controller import create_user
from app.users.controller import authenticate_user

from app.users.dependencies import get_current_user

from app.utils.jwt_handle import create_access_token

from app.users.models import user_model

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):
    return create_user(
        user_data,
        db
    )


@router.post(
    "/login",
    response_model=TokenResponse
)
def login_user(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        user_data.email,
        user_data.password,
        db
    )

    access_token = create_access_token({
        "user_id": user.id,
        "role": user.role
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get(
    "/me",
    response_model=UserResponse
)
def get_logged_in_user(
    current_user: user_model = Depends(get_current_user)
):
    return current_user