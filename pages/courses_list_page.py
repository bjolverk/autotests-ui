from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.empty_view = EmptyViewComponent(page, 'courses-list')

        self.course_view = CourseViewComponent(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar_view = CoursesListToolbarComponent(page)

        # self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        # self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(title='There is no results',
                                      description='Results from the load test pipeline will be displayed here')
