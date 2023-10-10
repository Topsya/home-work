from datetime import date
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


