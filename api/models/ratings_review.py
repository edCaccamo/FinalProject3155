from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class RatingReview(Base):
    __tablename__ = "ratings_reviews"

    id = Column(Integer, primary_key=True, index=True)
    review_text = Column(String, nullable=True)  # Optional text review
    score = Column(Integer, nullable=False)  # Numeric rating (e.g., 1-5 stars)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)

    # Relationships
    customer = relationship("Customer", back_populates="ratings_reviews")
    menu_item = relationship("MenuItem", back_populates="ratings_reviews")