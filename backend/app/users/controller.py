from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi import status


from app.users.models import user_model
from app.users.dtos import UserRegister
from app.utils.hashing import hash_password
from app.utils.hashing import verify_password


def get_user_by_email(
    email: str,
    db: Session
):
    return db.query(user_model).filter(
        user_model.email == email
    ).first()


def create_user(
    user_data: UserRegister,
    db: Session
):
    existing_user = get_user_by_email(
        user_data.email,
        db
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    new_user = user_model(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hash_password(
            user_data.password
        )
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def authenticate_user(
    email: str,
    password: str,
    db: Session
):
    user = get_user_by_email(
        email,
        db
    )

    if not user:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

    if not verify_password(
        password,
        user.hashed_password
    ):
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect password"
    )
    return user