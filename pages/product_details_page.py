from playwright.sync_api import Page
from pages.home_page import HomePage


class ProductDetailsPage(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.__product_name = self.page.get_by_text('Blue Top')
        self.__product_category = self.page.get_by_text('Category: Women > Tops')
        self.__product_price = self.page.get_by_text('Rs. 500')
        self.__product_availability = self.page.get_by_text('Availability:')
        self.__product_condition = self.page.get_by_text('Condition:')
        self.__product_brand = self.page.get_by_text('Brand:')
        self.__product_quantity_input = self.page.locator('[name="quantity"]')
        self.__add_to_cart_btn = self.page.locator('[class="btn btn-default cart"]')
        self.__view_cart_btn = self.page.get_by_text('View Cart')

    def check_products_details_is_displayed(self) -> None:
        assert self.__product_name.is_visible()
        assert self.__product_category.is_visible()
        assert self.__product_price.is_visible()
        assert self.__product_availability.is_visible()
        assert self.__product_condition.is_visible()
        assert self.__product_brand.is_visible()

    def increase_product_quantity(self, quantity) -> None:
        self.__product_quantity_input.click()
        self.__product_quantity_input.fill(str(quantity))

    def click_on_add_to_cart_btn(self) -> None:
        self.__add_to_cart_btn.click()

    def click_on_view_cart_btn(self) -> None:
        self.__view_cart_btn.click()