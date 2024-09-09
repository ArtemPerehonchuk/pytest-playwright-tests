from playwright.sync_api import Page
from pages.home_page import HomePage


class CheckoutPage(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.__address_details_title = self.page.get_by_text('Address Details')
        self.__review_your_order_title = self.page.get_by_text('Review Your Order')
        self.__description_input = self.page.locator('[class="form-control"]')
        self.__place_order_btn = self.page.get_by_text('Place Order')

    def check_checkout_titles_is_displayed(self) -> None:
        self.__address_details_title.is_visible()
        self.__review_your_order_title.is_visible()

    def fill_description_input(self, description) -> None:
        self.__description_input.scroll_into_view_if_needed()
        self.__description_input.fill(description)

    def click_on_place_order_btn(self) -> None:
        self.__place_order_btn.scroll_into_view_if_needed()
        self.__place_order_btn.click()