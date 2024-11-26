from fastapi.testclient import TestClient
from ..controllers import ratings_reviews as controller
from ..main import app
import pytest
from ..models import ratings_reviews as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_rating_review(db_session):
    # Create a sample rating review
    rating_review_data = {
        "review_text": "Delicious dish!",
        "score": 5,
        "customer_id": 1,
        "menu_item_id": 1
    }

    rating_review_object = model.RatingReview(**rating_review_data)

    # Call the create function
    created_rating_review = controller.create(db_session, rating_review_object)

    # Assertions
    assert created_rating_review is not None
    assert created_rating_review.review_text == "Delicious dish!"
    assert created_rating_review.score == 5
    assert created_rating_review.customer_id == 1
    assert created_rating_review.menu_item_id == 1
