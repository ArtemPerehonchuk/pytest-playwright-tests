from playwright.sync_api import Page
from pages.home_page import HomePage


class ViewCartPage(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.__first_product = self.page.get_by_text('Blue Top')
        self.__second_product = self.page.get_by_text('Men Tshirt')
        self.__first_product_price = self.page.locator('[class="cart_price"]:first-of-type')
        self.__second_product_price = self.page.locator('[class="cart_price"]:nth-of-type(2)')
        self.__first_product_quantity = self.page.locator('[class="disabled"]')
        self.__second_product_quantity = self.page.locator('[class="cart_quantity"]:nth-of-type(2)')
        self.__first_product_total_price = self.page.locator('[class="cart_total_price""]:first-of-type')
        self.__second_product_total_price = self.page.locator('[class="cart_total_price""]:nth-of-type(2)')
        self.__proceed_to_checkout_btn = self.page.get_by_text('Proceed To Checkout')
        self.__register_login_link = self.page.get_by_role("link", name="Register / Login")

    def check_first_product_is_displayed(self) -> None:
        assert self.__first_product.is_visible()

    def check_second_product_is_displayed(self) -> None:
        assert self.__second_product.is_visible()

    def verify_products_prices_and_quantity(self) -> None:
        assert self.__first_product_price.text_content() == 'Rs. 500'
        assert self.__second_product_price.text_content() == 'Rs. 400'
        assert self.__first_product_quantity.text_content() == '1'
        assert self.__second_product_quantity.text_content() == '2'
        assert self.__first_product_total_price.text_content() == 'Rs. 500'
        assert self.__second_product_total_price.text_content() == 'Rs. 400'

    def check_product_quantity(self, quantity) -> None:
        assert self.__first_product_quantity.text_content() == str(quantity)

    def click_on_proceed_to_checkout_btn(self) -> None:
        self.__proceed_to_checkout_btn.click()

    def click_on_register_login_link(self) -> None:
        self.__register_login_link.click()
