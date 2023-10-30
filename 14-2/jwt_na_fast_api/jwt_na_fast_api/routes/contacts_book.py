from typing import List

from fastapi import APIRouter, HTTPException, Depends, status, Path 
from sqlalchemy.orm import Session
from fastapi_limiter.depends import RateLimiter

from jwt_na_fast_api.database.db import get_db
from jwt_na_fast_api.schemas import ContactsBase, ContactMoedels
from jwt_na_fast_api.repository import contacts_book  as repository_contacts
from jwt_na_fast_api.repository.users import User
from jwt_na_fast_api.services.auth import auth_service

router = APIRouter(prefix='/contacts', tags=["contacts"])

@router.get("/", response_model=List[ContactMoedels], description='No more than 10 requests per minute',
             dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def read_contacts(  db: Session = Depends(get_db),
                        current_user: User = Depends(auth_service.get_current_user)):
    """
    The read_contacts function returns a list of cats.

    :param db: Session: Pass the database session to the function
    :param current_user: User: Get the current user
    :return: A list of  contacts
    :doc-author: Trelent
    """
    
    contacts = await repository_contacts.read_contacts(current_user, db)
    return contacts

@router.get("/{contact_id}", response_model=ContactMoedels)
async def read_contact(contact_id: int, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    """
    The read_contact function is a GET  contact with the given id.
    If no such  contact exists, it raises an HTTP 404 error.

    :param contact_id: int: the path parameter in the database.
    :param db: Session: Pass the database connection to the function
    :param current_user: User: Get the current user
    :return: A contact object
    :doc-author: Trelent
    """
    contact = await repository_contacts.read_contact(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.post("/", response_model=ContactMoedels, status_code= status.HTTP_201_CREATED)
async def create_contact(body: ContactsBase, db: Session = Depends(get_db),
                        current_user: User = Depends(auth_service.get_current_user) ):
    """
    Creates a new contact for a specific user.

    :param body: The data for the contact to create.
    :type body: ContactMoedels
    :param db: The database session.
    :type db: Session
    :param current_user: User: Get the current user
    :return: The newly created contact .
    :rtype: Contact 
     :doc-author: Trelent
    """
    return await repository_contacts.create_contact(body, current_user, db)

@router.put("/{contact_id}", response_model=ContactMoedels)
async def update_contact(body: ContactsBase, contact_id: int, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    """
    The update_contact function updates a contact in the database.
        The function takes three arguments:
            body: A dictionary containing the new values for each field of the contact to be updated.
            contact_id: An integer representing the id of the contact to be updated.
           
    
    :param body: ContactsBase: Get the data from the request body
    :param contact_id: int: Identify the contact to be updated
    :param db: Session: Get the database session
    :param current_user: User: Get the current user, which is used to check if the contact belongs to that user
    :return: A contact object
    :doc-author: Trelent
    """
    contact = await repository_contacts.update_contact(contact_id, body, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact  not found")
    return contact

@router.delete("/{contact_id}", response_model=ContactMoedels)
async def remove_contact(contact_id: int, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    """
    The remove_contact function removes a contact from the database.
        The function takes in an integer, contact_id, and uses it to find the corresponding
        Contact object in the database. If no such object exists, then a 404 error is raised. 
         
    :param contact_id: int: Specify the contact id of the contact to be removed
    :param db: Session: Pass the database session to the repository layer
    :param current_user: User: Get the user that is currently logged in
    :return: A contact object, but the function does not return a response
    :doc-author: Trelent
    """
    contact = await repository_contacts.remove_contact(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

@router.get("/{name}", response_model=ContactMoedels)
async def read_contact_by_name(name: str, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    """
    The read_contact function returns a contact by name.
    
    :param name: str: Specify the name of the contact that we want to read
    :param db: Session: Pass the database session to the repository layer
    :param current_user: User: Get the current user from the database
    :return: A contact object
    :doc-author: Trelent
    """
    contact = await repository_contacts.read_contact(name, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name in contacts not found")
    return contact

@router.get("/{surname}", response_model=ContactMoedels)
async def read_contact_by_suname(surname: str, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    """
    The read_contact function returns a contact by surname.
    
    :param surname: str: Get the surname from the url
    :param db: Session: Pass the database session to the repository layer
    :param current_user: User: Get the current user from the database
    :return: A dict with the following keys:
    :doc-author: Trelent
    """
    contact = await repository_contacts.read_contact(surname, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="surname in contacts not found")
    return contact

@router.get("/{email}", response_model=ContactMoedels)
async def read_contact_by_email(email: str, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    """
    The read_contact function returns a contact by email.
        
    
    :param email: str: Get the email of the contact to be read
    :param db: Session: Pass the database connection to the repository layer
    :param current_user: User: Get the user_id of the current user
    :return: A contact object
    :doc-author: Trelent
    """
    contact = await repository_contacts.read_contact(email, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email in contacts not found")
    return contact

@router.get("/{birthday}", response_model=ContactMoedels)
async def read_contact_days_to_birthday(days_to_birthday: int = Path(ge=0, le=7), db: Session = Depends(get_db)):
    """
    The read_contact_days_to_birthday function returns a list of contacts whose birthday is within the specified number of days.
        The default value for days_to_birthday is 7, which means that all contacts with birthdays in the next week will be returned.
        If no contact has a birthday within the specified number of days, an empty list will be returned.
    
    :param days_to_birthday: int: Specify the number of days to a birthday
    :param le: Limit the number of days to birthday
    :param db: Session: Access the database
    :return: A list of contacts
    :doc-author: Trelent
    """
    contacts = await repository_contacts.read_contact_days_to_birthday(db, days_to_birthday)
    return contacts



