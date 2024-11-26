from typing import Optional
from pydantic import BaseModel


class RatingReviewBase(BaseModel):
    review_text: Optional[str] = None
    score: int  # Rating score, e.g., 1-5


class RatingReviewCreate(RatingReviewBase):
    customer_id: int
    menu_item_id: int


class RatingReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    score: Optional[int] = None
    customer_id: Optional[int] = None
    menu_item_id: Optional[int] = None


class RatingReview(RatingReviewBase):
    id: int
    customer_id: int
    menu_item_id: int

    class Config:
        orm_mode = True
