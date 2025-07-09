from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state
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
