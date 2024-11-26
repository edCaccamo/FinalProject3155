from fastapi.testclient import TestClient
from ..controllers import customers as controller
from ..main import app
import pytest
from ..models import customers as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_customer(db_session):
    # Create a sample customer
    customer_data = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "phone_number": "1234567890",
        "address": "123 Main St"
    }

    customer_object = model.Customer(**customer_data)

    # Call the create function
    created_customer = controller.create(db_session, customer_object)

    # Assertions
    assert created_customer is not None
    assert created_customer.name == "Jane Doe"
    assert created_customer.email == "jane.doe@example.com"
    assert created_customer.phone_number == "1234567890"

