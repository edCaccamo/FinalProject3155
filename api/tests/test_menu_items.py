from fastapi.testclient import TestClient
from ..controllers import menu_items as controller
from ..main import app
import pytest
from ..models import menu_items as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_menu_item(db_session):
    # Create a sample menu item
    menu_item_data = {
        "dish_name": "Cheeseburger",
        "ingredients": "Bun, Beef Patty, Cheese",
        "price": 9.99,
        "calories": 800,
        "food_category": "Main Course"
    }

    menu_item_object = model.MenuItem(**menu_item_data)

    # Call the create function
    created_menu_item = controller.create(db_session, menu_item_object)

    # Assertions
    assert created_menu_item is not None
    assert created_menu_item.dish_name == "Cheeseburger"
    assert created_menu_item.ingredients == "Bun, Beef Patty, Cheese"
    assert created_menu_item.price == 9.99
    assert created_menu_item.calories == 800
    assert created_menu_item.food_category == "Main Course"
