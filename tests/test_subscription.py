import pytest

from data.test_data import TestData
from pages.home_page import HomePage
from pages.view_cart_page import ViewCartPage

home_page_url = 'https://automationexercise.com/'

user_email = TestData.email


class TestSubscription:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.view_cart_page = ViewCartPage(self.page)
        self.page.goto(home_page_url, wait_until='networkidle')

    def test_subscription_in_home_page(self, test_setup):
        """
        Test subscription in home page
        :param test_setup: setting up the browser and page objects
        :return:
        """
        self.home_page.verify_url(home_page_url)
        self.home_page.scroll_to_footer()
        self.home_page.check_subscription_title_is_displayed()
        self.home_page.fill_subscription_email_input(user_email)
        self.home_page.click_on_arrow_btn()
        self.home_page.check_success_subscribe_message_is_displayed()

    def test_subscription_in_cart_page(self, test_setup):
        """
        Test subscription in home page
        :param test_setup: setting up the browser and page objects
        :return:
        """
        self.home_page.verify_url(home_page_url)
        self.home_page.click_on_nav_menu_item('cart')
        self.view_cart_page.scroll_to_footer()
        self.view_cart_page.check_subscription_title_is_displayed()
        self.view_cart_page.fill_subscription_email_input(user_email)
        self.view_cart_page.click_on_arrow_btn()
        self.view_cart_page.check_success_subscribe_message_is_displayed()