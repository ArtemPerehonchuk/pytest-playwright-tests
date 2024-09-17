import pytest

from data.test_data import TestData
from pages.view_cart_page import ViewCartPage


class TestSubscription:

    @pytest.fixture
    def test_setup(self, new_page):
        self.view_cart_page = ViewCartPage(new_page)

    def test_subscription_in_home_page(self, test_setup):
        """
        Test subscription in home page
        :param test_setup: setting up the browser and page objects
        :return:
        """
        input_values = TestData.generate_input_values()

        self.view_cart_page.scroll_to_footer()
        self.view_cart_page.check_subscription_title_is_displayed()
        self.view_cart_page.fill_subscription_email_input(input_values["email"])
        self.view_cart_page.click_on_arrow_btn()
        self.view_cart_page.check_success_subscribe_message_is_displayed()

    def test_subscription_in_cart_page(self, test_setup):
        """
        Test subscription in home page
        :param test_setup: setting up the browser and page objects
        :return:
        """
        input_values = TestData.generate_input_values()

        self.view_cart_page.click_on_nav_menu_item('cart')
        self.view_cart_page.scroll_to_footer()
        self.view_cart_page.check_subscription_title_is_displayed()
        self.view_cart_page.fill_subscription_email_input(input_values["email"])
        self.view_cart_page.click_on_arrow_btn()
        self.view_cart_page.check_success_subscribe_message_is_displayed()