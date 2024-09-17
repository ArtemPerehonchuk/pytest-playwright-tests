import pytest

from data.test_data import TestData
from pages.view_cart_page import ViewCartPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.account_deleted_page import AccountDeletedPage

cart_page_url = TestData.cart_page_url


class TestCheckout:

    @pytest.fixture
    def test_setup(self, new_page):
        self.view_cart_page = ViewCartPage(new_page)
        self.login_page = LoginPage(new_page)
        self.signup_page = SignupPage(new_page)
        self.account_created_page = AccountCreatedPage(new_page)
        self.checkout_page = CheckoutPage(new_page)
        self.payment_page = PaymentPage(new_page)
        self.account_deleted_page = AccountDeletedPage(new_page)

    def test_register_while_checkout(self, test_setup):
        """Test user registration while checkout
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        input_values = TestData.generate_input_values()

        self.login_page.hover_on_product_and_click_add_to_cart_btn('blue top')
        self.login_page.click_on_view_cart_btn()
        self.view_cart_page.verify_url(cart_page_url)
        self.view_cart_page.click_on_proceed_to_checkout_btn()
        self.view_cart_page.click_on_register_login_link()
        self.login_page.fill_signup_inputs(input_values["name"], input_values["email"])
        self.login_page.click_on_signup_btn()
        self.signup_page.check_title_radio_btn('Mr')
        self.signup_page.fill_signup_inputs(input_values["password"])
        self.signup_page.select_day_from_days_drop_down()
        self.signup_page.select_month_from_months_drop_down()
        self.signup_page.select_year_from_years_drop_down()
        self.signup_page.check_newsletter_checkbox()
        self.signup_page.check_special_offers_checkbox()
        self.signup_page.fill_additional_signup_inputs()
        self.signup_page.select_country_from_countries_drop_down()
        self.signup_page.click_on_create_account_btn()
        self.account_created_page.check_account_created_title_is_displayed()
        self.account_created_page.click_on_continue_btn()
        self.view_cart_page.check_user_is_logged_in(input_values["name"])
        self.view_cart_page.click_on_nav_menu_item('cart')
        self.view_cart_page.click_on_proceed_to_checkout_btn()
        self.checkout_page.check_checkout_titles_is_displayed()
        self.checkout_page.fill_description_input(input_values["message"])
        self.checkout_page.click_on_place_order_btn()
        self.payment_page.fill_payment_details()
        self.payment_page.click_on_pay_and_confirm_order_btn()
        self.payment_page.check_success_message_is_displayed()
        self.payment_page.click_on_nav_menu_item('delete account')
        self.account_deleted_page.check_account_deleted_title_is_displayed()

    def test_register_before_checkout(self, test_setup):
        """Test user registration before checkout
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        input_values = TestData.generate_input_values()

        self.login_page.click_on_nav_menu_item('login')
        self.login_page.fill_signup_inputs(input_values["name"], input_values["email"])
        self.login_page.click_on_signup_btn()
        self.signup_page.check_title_radio_btn('Mr')
        self.signup_page.fill_signup_inputs(input_values["password"])
        self.signup_page.select_day_from_days_drop_down()
        self.signup_page.select_month_from_months_drop_down()
        self.signup_page.select_year_from_years_drop_down()
        self.signup_page.check_newsletter_checkbox()
        self.signup_page.check_special_offers_checkbox()
        self.signup_page.fill_additional_signup_inputs()
        self.signup_page.select_country_from_countries_drop_down()
        self.signup_page.click_on_create_account_btn()
        self.account_created_page.check_account_created_title_is_displayed()
        self.account_created_page.click_on_continue_btn()
        self.view_cart_page.check_user_is_logged_in(input_values["name"])
        self.view_cart_page.hover_on_product_and_click_add_to_cart_btn('blue top')
        self.view_cart_page.click_on_view_cart_btn()
        self.view_cart_page.verify_url(cart_page_url)
        self.view_cart_page.click_on_proceed_to_checkout_btn()
        self.checkout_page.check_checkout_titles_is_displayed()
        self.checkout_page.fill_description_input(input_values["message"])
        self.checkout_page.click_on_place_order_btn()
        self.payment_page.fill_payment_details()
        self.payment_page.click_on_pay_and_confirm_order_btn()
        self.payment_page.check_success_message_is_displayed()
        self.payment_page.click_on_nav_menu_item('delete account')
        self.account_deleted_page.check_account_deleted_title_is_displayed()


