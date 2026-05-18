from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi import status

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.users.models import user_model
from app.utils.jwt_handle import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/users/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    user = db.query(user_model).filter(
        user_model.id == payload.get("user_id")
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user
def admin_required(
    current_user = Depends(
        get_current_user
    )
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admins only"
        )

    return current_user

def get_current_admin(
    current_user: user_model = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    return current_user