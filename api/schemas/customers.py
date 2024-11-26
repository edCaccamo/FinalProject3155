from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: str
    address: Optional[str] = None


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None


class Customer(CustomerBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
