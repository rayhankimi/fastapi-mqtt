from pydantic import BaseModel, EmailStr, Field
from typing import Annotated


class SignUpSchema(BaseModel):
    """User signup model"""
    email: EmailStr
    username: Annotated[str, Field(min_length=3, max_length=20)]
    password: Annotated[str, Field(min_length=6, max_length=20)]


class LoginSchema(BaseModel):
    """User login model"""
    username: Annotated[str, Field(min_length=3, max_length=20)]
    password: Annotated[str, Field(min_length=6, max_length=20)]
