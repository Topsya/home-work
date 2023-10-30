from typing import List
from datetime import date, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import and_, extract, or_, select

from jwt_na_fast_api.database.models import  Contact, User
from jwt_na_fast_api.schemas import  ContactsBase, ContactMoedels


async def read_contacts(  user: User, db: Session) -> List[Contact]:
    """
    The read_contacts function returns a list of  contacts.

    :param user: The user to retrieve contacts for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: A list of contacts.
    :rtype: List[Contact]
    """
    return db.query(Contact).filter(Contact.user_id == user.id).all()

    

async def read_contact(contact_id: int, user: User, db: Session):
    """
    Retrieves a single contact with the specified ID for a specific user from the database.

    :param contact_id: The ID of the contact to retrieve.
    :type contact_id: int
    :param user: The user to retrieve the contact for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The contact with the specified ID, or None if it does not exist.
    :rtype: Contact | None
    """
    contact = db.query(Contact).filter_by(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    return contact



async def create_contact(body: ContactMoedels, user: User, db: Session) -> Contact:
    """
    Creates a new contact for a specific user.

    :param body: The data for the contact to create.
    :type body: ContactMoedels
    :param user: The user to create the contact for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The newly created contact .
    :rtype: Contact 
    """
    contacts = Contact(name=body.name, surname=body.surname, email=body.email,fonenamber=body.fonenamber, birthday= body.birthday, user_id=user.id)
    db.add(contacts)
    db.commit()
    db.refresh(contacts)
    return contacts


async def update_contact( contact_id: int, body: ContactsBase, user: User, db: Session) -> Contact | None:
    """
    Updates a single contact with the specified ID for a specific user.

    :param contact_id: The ID of the contact to update.
    :type contact_id: int
    :param body: The updated data for the contact.
    :type body: ContactsBase
    :param user: The user to update the contact  for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The updated contact, or None if it does not exist.
    :rtype: Contact | None
    """
    contact = db.query(Contact).filter(and_(Contact.id==contact_id,  Contact.user_id == user.id)).first()
    if contact:
        contact.name = body.name
        contact.surname = body.surname
        contact.email = body.email
        contact.fonenamber = body.fonenamber
        contact.birthday = body.birthday
 
        db.commit()
    return contact


async def remove_contact(contact_id: int, user: User, db: Session) -> Contact | None:
    """
    Removes a single contact with the specified ID for a specific user.

    :param contact_id: The ID of the contact to remove.
    :type contact_id: int
    :param user: The user to remove the contact for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The removed contact, or None if it does not exist.
    :rtype: Contact | None
    """
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

async def read_contact_by_name(name: str, user: User, db: Session):
    """
    The read_contacts function return  contact by name for a specific user from the database.

    :param name: The name of the contact to retrieve.
    :type name: str
    :param user: The user to retrieve the contact for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The contact with the name, or None if it does not exist.
    :rtype: Contact | None
    """
    contact = db.query(Contact).filter_by(and_(name=name, user= user.id  )).first()
    return contact

async def read_contact_by_surname(surname: str,  user: User, db: Session):
    """
    The read_contacts function return  contact by surname for a specific user from the database.

    :param surname: The surname of the contact to retrieve.
    :type surname: str
    :param user: The user to retrieve the contact for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The contact with the surname, or None if it does not exist.
    :rtype: Contact | None
    """
    contact = db.query(Contact).filter_by(and_(surname=surname, user=user.id)).first()
    return contact

async def read_contact_by_email(email: str, user: User, db: Session):
    """
    The read_contacts function return  contact by email for a specific user from the database.

    :param email: The email of the contact to retrieve.
    :type email: str
    :param user: The user to retrieve the contact for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The Contact with the email, or None if it does not exist.
    :rtype: Contact | None
    """
    contact = db.query(Contact).filter_by(and_(email=email, user= user.id)).first()
    return contact

async def read_contact_days_to_birthday(db: Session, days_to_birthday: int ):
    """
    The read_contact_days_to_birthday function return contacts whose birthday one week from today. 

    :param days_to_birthday: The days to birthday.
    :type days_to_birthday: int
    :param db: The database session.
    :type db: Session
    :return: The Contacts whose birthday one week, or None if it does not exist.
    :rtype: Contact | None
    """    
    today = date.today()
    end_date = today + timedelta(days=days_to_birthday)

    birthday_contacts  = (select(Contact).where(and_(Contact.birthday.isnot(None),
                extract("month", Contact.birthday) == end_date.month,
                extract("day", Contact.birthday) <= end_date.day,
                extract("month", Contact.birthday) >= today.month,)).order_by(Contact.birthday))

    upcoming_birthday  = await db.execute(birthday_contacts)
    results = upcoming_birthday.scalars().all()

    filtered_results = [contact for contact in results if (contact.birthday - today).days <= days_to_birthday]

    return filtered_results
