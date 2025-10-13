import allure

from elements.base_element import BaseElement
from playwright.sync_api import expect, Locator


class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(**kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.name}" to value {value}'):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Chacking that {self.type_of} "{self.name}" has a value {value}'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)

    def check_empty(self, nth: int = 0, **kwargs):
        with allure.step(f'Chacking that {self.type_of} "{self.name}" (number{nth}) is empty'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_empty()

    def check_editable(self, nth: int = 0, **kwargs):
        with allure.step(f'Chacking that {self.type_of} "{self.name}" (number{nth}) is editable'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_editable()
