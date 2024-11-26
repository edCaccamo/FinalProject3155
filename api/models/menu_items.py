from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    dish_name = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)  # Store as comma-separated strings or JSON if needed
    price = Column(Float, nullable=False)
    calories = Column(Integer, nullable=True)
    food_category = Column(String, nullable=True)  # e.g., "Appetizer", "Main Course", etc.

ratings_reviews = relationship("RatingReview", back_populates="menu_item")