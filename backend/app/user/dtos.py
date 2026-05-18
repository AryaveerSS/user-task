from pydantic import BaseModel,EmailStr,Field,field_validator,model_validator
from typing import Annotated,Optional
class user_schema(BaseModel):
    # id:int
    username:str
    email:EmailStr
    password:str