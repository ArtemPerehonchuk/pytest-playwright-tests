import pytest
import random

from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.view_cart_page import ViewCartPage
from data.test_data import TestData


class TestCart:

    @pytest.fixture
    def test_setup(self, new_page):
        self.view_cart_page = ViewCartPage(new_page)
        self.products_page = ProductsPage(new_page)
        self.product_details_page = ProductDetailsPage(new_page)

    def test_add_product(self, test_setup):
        """
        Add product to cart
        :param test_setup: setting up the browser and page objects
        :return:
        """
        self.view_cart_page.click_on_nav_menu_item('products')
        self.products_page.hover_on_product_and_click_add_to_cart_btn('blue top')
        self.products_page.click_on_continue_btn()
        self.products_page.hover_on_product_and_click_add_to_cart_btn('men tshirt')
        self.products_page.click_on_view_cart_btn()
        self.view_cart_page.check_first_product_is_displayed()
        self.view_cart_page.check_second_product_is_displayed()

    def test_product_quantity(self, test_setup):
        """
        Add product to cart
        :param test_setup: setting up the browser and page objects
        :return:
        """
        random_quantity = random.randint(2, 10)
        product_details_url = TestData.product_details_page_url

        self.view_cart_page.click_on_first_view_product_btn()
        self.product_details_page.verify_url(product_details_url)
        self.product_details_page.increase_product_quantity(random_quantity)
        self.product_details_page.click_on_add_to_cart_btn()
        self.product_details_page.click_on_view_cart_btn()
        self.view_cart_page.check_product_quantity(random_quantity)


