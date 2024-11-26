from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class PaymentInfo(Base):
    __tablename__ = "payment_info"

    id = Column(Integer, primary_key=True, index=True)
    card_info = Column(String, nullable=False)  # Typically encrypted or tokenized in a real system
    trans_status = Column(String, nullable=False)  # e.g., "Success", "Pending", "Failed"
    payment_type = Column(String, nullable=False)  # e.g., "Credit Card", "PayPal", etc.
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)

    # Relationship to the orders table
    order = relationship("Order", back_populates="payment_info")