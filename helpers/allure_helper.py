import allure


def attach_response_to_allure(resp, name="Response"):
    """Attach JSON response to Allure report"""
    allure.attach(
        str(resp.json()),
        name=name,
        attachment_type=allure.attachment_type.JSON
    )
