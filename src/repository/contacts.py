from typing import Type

from sqlalchemy.orm import Session
from src.database.models import Contact, User
from src.schemas import ContactModel
from sqlalchemy import and_

async def get_contacts(skip: int, limit: int, db: Session) -> list[Type[Contact]]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Type[Contact] | None:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(phone_number=body.phone_number)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactModel, db: Session, user: User) -> Contact | None:
    contact = (db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first())
    if contact:
        contact.phone_number = body.phone_number
        db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session, user: User) -> Contact | None:
    contact = (db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first())
    if contact:
        db.delete(contact)
        db.commit()
    return contact