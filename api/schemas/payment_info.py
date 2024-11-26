from typing import Optional
from pydantic import BaseModel


class PaymentInfoBase(BaseModel):
    card_info: str  # Ensure sensitive info is tokenized/encrypted
    trans_status: str  # E.g., "Success", "Pending", "Failed"
    payment_type: str  # E.g., "Credit Card", "PayPal", etc.


class PaymentInfoCreate(PaymentInfoBase):
    order_id: int


class PaymentInfoUpdate(BaseModel):
    card_info: Optional[str] = None
    trans_status: Optional[str] = None
    payment_type: Optional[str] = None
    order_id: Optional[int] = None


class PaymentInfo(PaymentInfoBase):
    id: int
    order_id: int

    class Config:
        orm_mode = True
