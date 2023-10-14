from typing import List

from fastapi import APIRouter, HTTPException, Depends, status, Path
from sqlalchemy.orm import Session

from jwt_na_fast_api.database.db import get_db
from jwt_na_fast_api.schemas import ContactsBase, ContactMoedels
from jwt_na_fast_api.repository import contacts_book  as repository_contacts
from jwt_na_fast_api.repository.users import User
from jwt_na_fast_api.services.auth import auth_service

router = APIRouter(prefix='/contacts', tags=["contacts"])

@router.get("/", response_model=List[ContactMoedels])
async def read_contacts(  db: Session = Depends(get_db),
                        current_user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contacts.read_contacts(current_user, db)
    return contacts

@router.get("/{contact_id}", response_model=ContactMoedels)
async def read_contact(contact_id: int, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.read_contact(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.post("/", response_model=ContactMoedels, status_code= status.HTTP_201_CREATED)
async def create_contact(body: ContactsBase, db: Session = Depends(get_db),
                        current_user: User = Depends(auth_service.get_current_user) ):
    return await repository_contacts.create_contact(body, current_user, db)

@router.put("/{contact_id}", response_model=ContactMoedels)
async def update_contact(body: ContactsBase, contact_id: int, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.update_contact(contact_id, body, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact  not found")
    return contact

@router.delete("/{contact_id}", response_model=ContactMoedels)
async def remove_contact(contact_id: int, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.remove_contacts(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

@router.get("/{name}", response_model=ContactMoedels)
async def read_contact(name: str, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.read_contact(name, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name in contacts not found")
    return contact

@router.get("/{surname}", response_model=ContactMoedels)
async def read_contact(surname: str, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.read_contact(surname, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="surname in contacts not found")
    return contact

@router.get("/{email}", response_model=ContactMoedels)
async def read_contact(email: str, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.read_contact(email, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email in contacts not found")
    return contact

@router.get("/{birthday}", response_model=ContactMoedels)
async def read_contact_days_to_birthday(days_to_birthday: int = Path(ge=0, le=7), db: Session = Depends(get_db)):
    contacts = await repository_contacts.read_contact_days_to_birthday(db, days_to_birthday)
    return contacts

