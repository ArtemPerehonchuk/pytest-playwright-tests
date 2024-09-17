import pytest

from data.test_data import TestData
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage
from pages.account_deleted_page import AccountDeletedPage

login_page_url = TestData.login_page_url

correct_user_email = TestData.valid_user_email
correct_user_password = TestData.valid_user_password
correct_user_name = TestData.valid_user_name


class TestRegisterAndLogin:

    @pytest.fixture
    def test_setup(self, new_page):
        self.login_page = LoginPage(new_page)
        self.signup_page = SignupPage(new_page)
        self.account_created_page = AccountCreatedPage(new_page)
        self.account_deleted_page = AccountDeletedPage(new_page)

    def test_register_user(self, test_setup):
        """Test user registration
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        input_values = TestData.generate_input_values()

        self.login_page.click_on_nav_menu_item('signup')
        self.login_page.check_new_user_signup_title_is_displayed()
        self.login_page.fill_signup_inputs(input_values["name"], input_values["email"])
        self.login_page.click_on_signup_btn()
        self.signup_page.check_enter_account_info_title_is_displayed()
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
        self.account_created_page.check_user_is_logged_in(input_values["name"])
        self.account_created_page.click_on_nav_menu_item('delete account')
        self.account_deleted_page.check_account_deleted_title_is_displayed()

    def test_valid_login(self, test_setup):
        """
        Login user with correct email and password
        :param test_setup: setting up the browser and page objects
        :return:
        """
        self.login_page.click_on_nav_menu_item('signup')
        self.login_page.check_login_to_your_account_title_is_displayed()
        self.login_page.fill_login_inputs(correct_user_email, correct_user_password)
        self.login_page.click_on_login_btn()
        self.login_page.check_user_is_logged_in(correct_user_name)

    def test_invalid_login(self, test_setup):
        """
        Login user with incorrect email and password
        :param test_setup: setting up the browser and page objects
        :return:
        """
        input_values = TestData.generate_input_values()

        self.login_page.click_on_nav_menu_item('signup')
        self.login_page.check_login_to_your_account_title_is_displayed()
        self.login_page.fill_login_inputs(input_values["email"], input_values["password"])
        self.login_page.click_on_login_btn()
        self.login_page.check_login_error_message_is_displayed()

    def test_logout(self, test_setup):
        """
        Logout user
        :param test_setup: setting up the browser and page objects
        :return:
        """
        self.login_page.click_on_nav_menu_item('signup')
        self.login_page.check_login_to_your_account_title_is_displayed()
        self.login_page.fill_login_inputs(correct_user_email, correct_user_password)
        self.login_page.click_on_login_btn()
        self.login_page.check_user_is_logged_in(correct_user_name)
        self.login_page.click_on_nav_menu_item('logout')
        self.login_page.verify_url(login_page_url)

    def test_register_user_with_existing_email(self, test_setup):
        """Test user registration with existing email
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        input_values = TestData.generate_input_values()

        self.login_page.click_on_nav_menu_item('signup')
        self.login_page.check_new_user_signup_title_is_displayed()
        self.login_page.fill_signup_inputs(input_values["name"], correct_user_email)
        self.login_page.click_on_signup_btn()
        self.login_page.check_signup_error_message_is_displayed()







