from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(Date, nullable=False)
    tracking_num = Column(String, unique=True, nullable=False)
    status = Column(String, nullable=False)
    total_price = Column(Float, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    order_details = relationship("OrderDetail", back_populates="orders")
    customer = relationship("Customer", back_populates="orders")