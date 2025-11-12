import pytest
import helpers.user_helper as user_helper


@pytest.fixture
def new_user():
    """
    Fixture to create a new user before the test and delete it afterward.
    """
    user = user_helper.generate_user_data()
    response = user_helper.create_user(user)
    assert response.status_code == 200, (
        f"User creation failed: {response.text}"
    )
    yield user
