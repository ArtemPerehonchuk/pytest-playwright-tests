from playwright.sync_api import Page
from pages.home_page import HomePage


class AccountDeletedPage(HomePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.__account_deleted_title = self.page.locator('[data-qa="account-deleted"]')
        self.__continue_btn = self.page.locator('[data-qa="continue-button"]')

    def check_account_deleted_title_is_displayed(self) -> None:
        assert self.__account_deleted_title.is_visible()

