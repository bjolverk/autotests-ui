from playwright.sync_api import sync_playwright, expect

TEST_DATA = {
    "email": "user.name@gmail.com",
    "username": "username",
    "password": "password"
}

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")

    username_input = page.get_by_test_id("registration-form-username-input").locator("input")

    password_input = page.get_by_test_id("registration-form-password-input").locator("input")

    registration_button = page.get_by_test_id("registration-page-registration-button")

    for field in [email_input, username_input, password_input]:
        expect(field).to_be_visible()
        expect(field).to_be_editable()
        expect(field).to_be_empty()

    expect(registration_button).to_be_visible()
    expect(registration_button).to_be_disabled()

    # Заполняем форму
    email_input.focus()
    page.keyboard.type(TEST_DATA["email"], delay=100)
    expect(email_input).to_have_value(TEST_DATA["email"])

    username_input.focus()
    page.keyboard.type(TEST_DATA["username"], delay=100)
    expect(username_input).to_have_value(TEST_DATA["username"])

    password_input.focus()
    page.keyboard.type(TEST_DATA["password"], delay=100)
    expect(password_input).to_have_value(TEST_DATA["password"])

    # Проверяем кнопку
    expect(registration_button).to_be_enabled()

    page.wait_for_timeout(5000)
