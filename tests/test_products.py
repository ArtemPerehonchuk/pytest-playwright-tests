import pytest

from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from data.test_data import TestData

products_page_url = TestData.products_page_url
product_details_url = TestData.product_details_page_url


class TestProducts:

    @pytest.fixture
    def test_setup(self, new_page):
        self.products_page = ProductsPage(new_page)
        self.product_details_page = ProductDetailsPage(new_page)

    def test_product_detail(self, test_setup):
        """
        Verify All Products and product detail page
        :param test_setup: setting up the browser and page objects
        :return:
        """
        self.products_page.click_on_nav_menu_item('products')
        self.products_page.verify_url(products_page_url)
        self.products_page.check_products_list_is_displayed()
        self.products_page.click_on_first_view_product_btn()
        self.product_details_page.verify_url(product_details_url)
        self.product_details_page.check_products_details_is_displayed()

    def test_product_search(self, test_setup):
        """
        Search for product
        :param test_setup: setting up the browser and page objects
        :return:
        """
        self.products_page.click_on_nav_menu_item('products')
        self.products_page.verify_url(products_page_url)
        self.products_page.check_products_list_is_displayed()
        self.products_page.search_product()
        self.products_page.check_search_results()