from playwright.sync_api import sync_playwright, expect



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    expect(email_input).to_be_visible()

    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    expect(username_input).to_be_visible()

    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    expect(password_input).to_be_visible()

    registration_button = page.get_by_test_id("registration-page-registration-button")
    expect(registration_button).to_be_visible()
    expect(registration_button).to_be_disabled()

    email_input.fill("user.name@gmail.com")
    expect(email_input).to_have_value("user.name@gmail.com")
    expect(registration_button).to_be_disabled()

    username_input.fill("username")
    expect(username_input).to_have_value("username")
    expect(registration_button).to_be_disabled()

    password_input.fill("password")
    expect(password_input).to_have_value("password")
    expect(registration_button).to_be_enabled()

    registration_button.click()

    expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    dashbord_label = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashbord_label).to_have_text("Dashboard")



    page.wait_for_timeout(5000)
