import requests
from requests import Response
from faker import Faker
from config import BASE_URL


fake = Faker()
TIMEOUT = 10


def generate_user_data() -> dict:
    """Generate random user data using Faker."""
    return {
        "id": fake.random_int(min=1000, max=9999),
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(length=10, special_chars=True),
        "phone": fake.phone_number(),
        "userStatus": 1
    }


def create_user(user_data: dict) -> Response:
    """Create a user via POST request."""
    return requests.post(f"{BASE_URL}/user", json=user_data, timeout=TIMEOUT)


def update_user(username: str, user_data: dict) -> Response:
    """Update a user via PUT request."""
    return requests.put(
        f"{BASE_URL}/user/{username}",
        json=user_data,
        timeout=TIMEOUT
        )


def get_user(username: str) -> Response:
    """Get a user by username via GET request."""
    return requests.get(f"{BASE_URL}/user/{username}", timeout=TIMEOUT)


def delete_user(username: str) -> Response:
    """Delete a user via DELETE request."""
    return requests.delete(f"{BASE_URL}/user/{username}", timeout=TIMEOUT)


def login_user(username: str, password: str) -> Response:
    """Logs user into the system via GET request."""
    return requests.get(
      f"{BASE_URL}/user/login?username={username}&password={password}",
      timeout=TIMEOUT
    )


def logout_user() -> Response:
    """Logs out user from the system via GET request."""
    return requests.get(f"{BASE_URL}/user/logout", timeout=TIMEOUT)
