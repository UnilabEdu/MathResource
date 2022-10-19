import pytest

from models.models import User
from src import create_app


@pytest.fixture
def test_app():
    app = create_app()
    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!


def test_check_user_from_db(test_app):
    """
    GIVEN User mail
    WHEN a new User is created
    THEN check if user with the same mail already exists
    """

    user_mail = "email"
    user_from_db = User.query.filter_by(email=user_mail).first()
    assert user_from_db


def test_two():
    assert True


def test_three():
    assert True


def test_four():
    assert True
