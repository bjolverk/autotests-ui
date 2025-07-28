from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email = page.get_by_test_id('login-form-email-input').locator('input')
        self.password = page.get_by_test_id('login-form-password-input').locator('input')
        self.form_сontainer =page.locator('(//div[@class="MuiBox-root css-0"])[2]')

    def fill(self, email: str, password: str):
        self.email.fill(email)
        expect(self.email).to_have_value(email)

        self.password.fill(password)
        expect(self.password).to_have_value(password)

    def check_visible(self, email: str = None, password: str = None ):
        expect(self.form_сontainer).to_be_visible()

        expect(self.email).to_be_visible()
        if email is not None:
            expect(self.email).to_have_value(email)
        else:
            expect(self.email).to_be_empty()
            expect(self.email).to_be_editable()

        expect(self.password).to_be_visible()
        if password is not None:
            expect(self.password).to_have_value(password)
        else:
            expect(self.password).to_be_empty()
            expect(self.password).to_be_editable()
