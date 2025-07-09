from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    """
    Тест сохранён на всякий случай.
    :return:
    """
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
        expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_label = page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_label).to_have_text("Dashboard")

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_label = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_label).to_be_visible()
        expect(courses_label).to_have_text('Courses')

        folder_icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(folder_icon).to_be_visible()

        sub_header_6 = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(sub_header_6).to_be_visible()
        expect(sub_header_6).to_have_text('There is no results')

        result_paragraph = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(result_paragraph).to_be_visible()
        expect(result_paragraph).to_have_text('Results from the load test pipeline will be displayed here')
