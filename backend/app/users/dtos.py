from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import field_validator
from datetime import datetime


class UserRegister(BaseModel):
    name: str

    email: EmailStr

    password: str
    @field_validator("name")
    @classmethod
    def validate_name(cls, value):

        if len(value) < 3:
            raise ValueError(
                "Name should have at least 3 characters"
            )

        if len(value) > 50:
            raise ValueError(
                "Name cannot exceed 50 characters"
            )

        return value
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, value):

        if len(value) < 6:
            raise ValueError(
                "Password should have at least 6 characters"
            )

        if len(value) > 72:
            raise ValueError(
                "Password cannot exceed 72 characters"
            )

        return value

class UserLogin(BaseModel):
    email: EmailStr
    password: str


    @field_validator("password")
    @classmethod
    def validate_password(cls, value):

        if len(value) < 6:
            raise ValueError(
                "Password should have at least 6 characters"
            )

        return value


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True


class TokenUser(BaseModel):
    id: int
    name: str
    email: str
    role: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: TokenUser