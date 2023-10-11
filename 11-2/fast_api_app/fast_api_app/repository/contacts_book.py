from typing import List
from datetime import date, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import and_, extract, or_, select

from fast_api_app.database.models import Contact
from fast_api_app.schemas import  ContactsBase, ContactMoedels

async def read_contacts( db: Session) -> List[Contact]:
    return db.query(Contact).all()


async def read_contact(contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact



async def create_contact(body: ContactMoedels, db: Session) -> Contact:
    contacts = Contact(name=body.name, surname=body.surname, email=body.email,fonenamber=body.fonenamber, birthday= body.birthday)
    db.add(contacts)
    db.commit()
    db.refresh(contacts)
    return contacts

async def update_contact(body: ContactsBase, contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    if contact:
        contact.name = body.name
        contact.surname = body.surname
        contact.email = body.email
        contact.fonenamber = body.fonenamber
        contact.birthday = body.birthday
 
        db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

async def read_contact(name: str, db: Session):
    contact = db.query(Contact).filter_by(name=name ).first()
    return contact

async def read_contact(surname: str, db: Session):
    contact = db.query(Contact).filter_by(surname=surname).first()
    return contact

async def read_contact(email: str, db: Session):
    contact = db.query(Contact).filter_by(email=email).first()
    return contact

async def read_contact_days_to_birthday(db: Session, days_to_birthday: int ):
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
