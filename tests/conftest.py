import pytest
from playwright.sync_api import sync_playwright, Page, Playwright, expect


#
# @pytest.fixture
# def chromium_page() -> Page:
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         yield browser.new_page()
#         browser.close()


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Регистрация пользователя
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    page.get_by_test_id("registration-form-email-input").locator("input").fill("user.name@gmail.com")
    page.get_by_test_id("registration-form-username-input").locator("input").fill("username")
    page.get_by_test_id("registration-form-password-input").locator("input").fill("password")
    page.get_by_test_id("registration-page-registration-button").click()

    # Проверка успешной регистрации
    expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    # Сохранение состояния
    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page
    browser.close()
