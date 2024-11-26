from fastapi.testclient import TestClient
from ..controllers import payment_info as controller
from ..main import app
import pytest
from ..models import payment_info as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_payment_info(db_session):
    # Create a sample payment info
    payment_info_data = {
        "card_info": "1234-5678-9876-5432",
        "trans_status": "Success",
        "payment_type": "Credit Card",
        "order_id": 1
    }

    payment_info_object = model.PaymentInfo(**payment_info_data)

    # Call the create function
    created_payment_info = controller.create(db_session, payment_info_object)

    # Assertions
    assert created_payment_info is not None
    assert created_payment_info.card_info == "1234-5678-9876-5432"
    assert created_payment_info.trans_status == "Success"
    assert created_payment_info.payment_type == "Credit Card"
    assert created_payment_info.order_id == 1
