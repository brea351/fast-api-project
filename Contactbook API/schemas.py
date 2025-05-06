from pydantic import BaseModel
from typing import List, Optional

class AddressCreate(BaseModel):
    street: str
    city: str
    country: str

class TagCreate(BaseModel):
    tag_name: str

class ContactCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str]
    addresses: List[AddressCreate] = []
    tags: List[TagCreate] = []

class ContactOut(ContactCreate):
    id: int
    class Config:
        orm_mode = True
