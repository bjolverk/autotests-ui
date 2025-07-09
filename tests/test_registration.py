import pytest
from playwright.sync_api import sync_playwright, expect, Page



TEST_DATA = {
    "email": "user.name@gmail.com",
    "username": "username",
    "password": "password"
}


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = chromium_page.get_by_test_id("registration-form-email-input").locator("input")

    username_input = chromium_page.get_by_test_id("registration-form-username-input").locator("input")

    password_input = chromium_page.get_by_test_id("registration-form-password-input").locator("input")

    registration_button = chromium_page.get_by_test_id("registration-page-registration-button")

    for field in [email_input, username_input, password_input]:
        expect(field).to_be_visible()
        expect(field).to_be_editable()
        expect(field).to_be_empty()

    email_input.fill(TEST_DATA['email'])
    username_input.fill(TEST_DATA['username'])
    password_input.fill(TEST_DATA['password'])

    registration_button.click()
    dashbord_label = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashbord_label).to_be_visible()
