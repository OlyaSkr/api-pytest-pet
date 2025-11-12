"""
    Tests api response.
"""
import allure
import helpers.user_helper as user_helper
import helpers.allure_helper as allure_helper


@allure.feature("User Management")
@allure.story("Register User")
@allure.severity(allure.severity_level.CRITICAL)
def test_register_user():
    """Test registering a new user."""
    user = user_helper.generate_user_data()
    resp = user_helper.create_user(user)

    allure_helper.attach_response_to_allure(resp, "Register User Response")

    error_msg = f"Expected 200, got {resp.status_code}: {resp.text}"
    assert resp.status_code == 200, error_msg
    assert resp.json().get("code") == 200
    assert resp.json().get("message") == str(user["id"])

    user_helper.delete_user(user["username"])


@allure.feature("User Management")
@allure.story("Update User")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_user(new_user):
    """Test updating an existing user."""
    resp = user_helper.update_user(new_user["username"], new_user)
    resp_json = resp.json()

    allure_helper.attach_response_to_allure(resp, "Update User Response")

    assert resp.status_code == 200
    assert resp_json.get("code") == 200
    assert resp_json.get("message") == str(new_user["id"])


@allure.feature("User Management")
@allure.story("Get User")
@allure.severity(allure.severity_level.NORMAL)
def test_get_user_by_username(new_user):
    """Test retrieving a user by username."""
    resp = user_helper.get_user(new_user["username"])

    allure_helper.attach_response_to_allure(resp, "Get User Response")

    assert resp.status_code == 200
    user_data = resp.json()
    assert user_data["username"] == new_user["username"]

    user_helper.delete_user(new_user["username"])


@allure.feature("User Management")
@allure.story("Delete User")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_user(new_user):
    """Test deleting a user by username."""
    resp = user_helper.delete_user(new_user["username"])

    allure_helper.attach_response_to_allure(resp, "Delete User Response")

    assert resp.status_code == 200
    assert resp.json().get("code") == 200
    assert resp.json().get("message") == new_user["username"]


@allure.feature("User Management")
@allure.story("Get User After Deletion")
@allure.severity(allure.severity_level.NORMAL)
def test_get_user_after_deletion(new_user):
    """Test that retrieving a user after deletion returns 404."""
    resp = user_helper.delete_user(new_user["username"])
    assert resp.status_code == 200

    resp = user_helper.get_user(new_user["username"])

    allure_helper.attach_response_to_allure(
        resp, "Get User After Deletion Response"
        )

    assert resp.status_code == 404
    resp_json = resp.json()
    assert resp_json.get("code") == 1
    assert resp_json.get("type") == "error"
    assert resp_json.get("message") == "User not found"


@allure.feature("User Management")
@allure.story("Login and Logout")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_logout_user_to_system(new_user):
    """Test login uaer to the system and logout from the system"""
    resp = user_helper.login_user(new_user["username"], new_user["password"])
    allure_helper.attach_response_to_allure(resp, "Login Response")
    resp_json = resp.json()

    assert resp.status_code == 200
    assert resp_json.get("code") == 200

    resp = user_helper.logout_user()
    allure_helper.attach_response_to_allure(resp, "Logout Response")
    resp_json = resp.json()

    assert resp.status_code == 200
    assert resp_json.get("code") == 200
    assert resp_json.get("message") == "ok"

    user_helper.delete_user(new_user["username"])
