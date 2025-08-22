from components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email = Input(page, 'login-form-email-input', 'Email')
        self.password = Input(page, 'login-form-password-input', 'Password')

    def fill(self, email: str, password: str):
        self.email.fill(email)

        self.email.check_have_value(email)

        self.password.fill(password)

        self.password.check_have_value(password)

    def check_visible(self, email: str = None, password: str = None):

        self.email.check_visible()
        if email is not None:
            self.email.check_have_value(email)
        else:
            self.email.check_empty()
            self.email.check_editable()

        self.password.check_visible()
        if password is not None:
            self.password.check_have_value(password)
        else:
            self.password.check_empty()
            self.password.check_editable()
