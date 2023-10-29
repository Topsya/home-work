from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr


class ContactsBase(BaseModel):
    name : str
    surname : str
    email : EmailStr
    fonenamber : str
    birthday : date

class ContactMoedels(ContactsBase):
    id  : int
     
    class Config:
        from_attributes = True


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=10)


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RequestEmail(BaseModel):
    email: EmailStr
