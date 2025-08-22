from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.link import Link
from pages.base_page import BasePage
from elements.button import Button


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form_component = RegistrationFormComponent(page)

        self.registration_button = Button(page, "registration-page-registration-button", "Registration")

        self.login_link = Link(page, 'registration-page-login-link', "Login")

    def fill_registration_form(self, email: str, username: str, password: str):
        self.registration_form_component.check_visible()
        self.registration_form_component.fill(email=email, username=username, password=password)
        self.registration_form_component.check_visible(email=email, username=username, password=password)

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
