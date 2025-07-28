import time

import pytest
from playwright.sync_api import sync_playwright, expect, Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

TEST_DATA = {
    "email": "user.name@gmail.com",
    "username": "username",
    "password": "password"
}


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(email=TEST_DATA["email"],
                                             username=TEST_DATA["username"],
                                             password=TEST_DATA["password"])
    registration_page.click_registration_button()

    dashboard_page.check_dashboard_url()
    dashboard_page.check_visible_dashboard_title()
    time.sleep(5)
