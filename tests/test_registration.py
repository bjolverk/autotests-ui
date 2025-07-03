from playwright.sync_api import sync_playwright, expect

def test_successful_registration():
    TEST_DATA = {
        "email": "user.name@gmail.com",
        "username": "username",
        "password": "password"
    }

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id("registration-form-email-input").locator("input")

        username_input = page.get_by_test_id("registration-form-username-input").locator("input")

        password_input = page.get_by_test_id("registration-form-password-input").locator("input")

        registration_button = page.get_by_test_id("registration-page-registration-button")

        for field in [email_input, username_input, password_input]:
            expect(field).to_be_visible()
            expect(field).to_be_editable()
            expect(field).to_be_empty()

        email_input.fill(TEST_DATA['email'])
        username_input.fill(TEST_DATA['username'])
        password_input.fill(TEST_DATA['password'])

        registration_button.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()
        # page = browser.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')