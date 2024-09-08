from playwright.sync_api import Page
from pages.home_page import HomePage


class AccountCreatedPage(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.__account_created_title = self.page.locator('[data-qa="account-created"]')
        self.__continue_btn = self.page.locator('[data-qa="continue-button"]')

    def check_account_created_title_is_displayed(self) -> None:
        assert self.__account_created_title.is_visible()

    def click_on_continue_btn(self) -> None:
        self.__continue_btn.click()