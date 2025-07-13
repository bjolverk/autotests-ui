from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    'email, password',
    [("user.name@gmail.com", "password"),
     ("user.name@gmail.com", "  "),
     ("  ", "password")]
)
def test_wrong_email_or_password_authorization(chromium_page: Page, email, password):
    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     page = browser.new_page()
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    # email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input = chromium_page.get_by_test_id("login-form-email-input").locator('//div//input')
    # email_input.fill('user.name@gmail.com')
    email_input.fill(email)

    # password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input = chromium_page.get_by_test_id("login-form-password-input").locator('input')

    # password_input.fill('Password')
    password_input.fill(password)

    # login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    login_button = chromium_page.get_by_test_id("login-page-login-button")
    login_button.click()

    wrong_email_or_password_alert = chromium_page.locator('//div[@class="MuiAlert-message css-1xsto0d"]')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')
