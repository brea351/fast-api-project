from sqlalchemy.orm import Session
import models, schemas

def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.Contact(name=contact.name, email=contact.email, phone=contact.phone)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)

    for addr in contact.addresses:
        db.add(models.Address(contact_id=db_contact.id, **addr.dict()))
    
    for tag in contact.tags:
        db.add(models.Tag(contact_id=db_contact.id, **tag.dict()))

    db.commit()
    return db_contact

def get_contacts(db: Session):
    return db.query(models.Contact).all()

def update_contact(db: Session, contact_id: int, contact: schemas.ContactCreate):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if not db_contact:
        return None
    for field, value in contact.dict(exclude_unset=True).items():
        setattr(db_contact, field, value)
    db.commit()
    return db_contact

def delete_contact(db: Session, contact_id: int):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact
