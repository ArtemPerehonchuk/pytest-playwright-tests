import pytest

from data.test_data import TestData
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage
from pages.account_deleted_page import AccountDeletedPage

home_page_url = 'https://automationexercise.com/'
login_page_url = 'https://automationexercise.com/login'

user_name = TestData.name
user_email = TestData.email
user_password = TestData.password
user_first_name = TestData.first_name
user_last_name = TestData.last_name
user_company = TestData.company
user_address = TestData.address
user_address2 = TestData.address2
user_state = TestData.state
user_city = TestData.city
user_zipcode = TestData.zipcode
user_phone_number = TestData.mobile_number
correct_user_email = TestData.valid_user_email
correct_user_password = TestData.valid_user_password
correct_user_name = TestData.valid_user_name


class TestRegisterAndLogin:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.login_page = LoginPage(self.page)
        self.signup_page = SignupPage(self.page)
        self.account_created_page = AccountCreatedPage(self.page)
        self.account_deleted_page = AccountDeletedPage(self.page)

        self.page.goto(home_page_url, wait_until='networkidle', timeout=60000)

    def test_register_user(self, test_setup):
        """Test user registration
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.home_page.verify_url(home_page_url)
        self.home_page.click_on_nav_menu_item('signup')
        self.login_page.check_new_user_signup_title_is_displayed()
        self.login_page.fill_signup_inputs(user_name, user_email)
        self.login_page.click_on_signup_btn()
        self.signup_page.check_enter_account_info_title_is_displayed()
        self.signup_page.check_title_radio_btn('Mr')
        self.signup_page.fill_signup_inputs(user_password)
        self.signup_page.select_day_from_days_drop_down()
        self.signup_page.select_month_from_months_drop_down()
        self.signup_page.select_year_from_years_drop_down()
        self.signup_page.check_newsletter_checkbox()
        self.signup_page.check_special_offers_checkbox()
        self.signup_page.fill_additional_signup_inputs(user_first_name, user_last_name, user_company, user_address, user_address2, user_state, user_city, user_zipcode, user_phone_number)
        self.signup_page.select_country_from_countries_drop_down()
        self.signup_page.click_on_create_account_btn()
        self.account_created_page.check_account_created_title_is_displayed()
        self.account_created_page.click_on_continue_btn()
        self.home_page.check_user_is_logged_in(user_name)
        self.home_page.click_on_nav_menu_item('delete account')
        self.account_deleted_page.check_account_deleted_title_is_displayed()

    def test_valid_login(self, test_setup):
        """
        Login user with correct email and password
        :param test_setup: setting up the browser and page objects
        :return:
        """
        self.home_page.verify_url(home_page_url)
        self.home_page.click_on_nav_menu_item('signup')
        self.login_page.check_login_to_your_account_title_is_displayed()
        self.login_page.fill_login_inputs(correct_user_email, correct_user_password)
        self.login_page.click_on_login_btn()
        self.home_page.check_user_is_logged_in(correct_user_name)

    def test_invalid_login(self, test_setup):
        """
        Login user with incorrect email and password
        :param test_setup: setting up the browser and page objects
        :return:
        """
        self.home_page.verify_url(home_page_url)
        self.home_page.click_on_nav_menu_item('signup')
        self.login_page.check_login_to_your_account_title_is_displayed()
        self.login_page.fill_login_inputs(user_email, user_password)
        self.login_page.click_on_login_btn()
        self.login_page.check_login_error_message_is_displayed()

    def test_logout(self, test_setup):
        """
        Logout user
        :param test_setup: setting up the browser and page objects
        :return:
        """
        self.home_page.verify_url(home_page_url)
        self.home_page.click_on_nav_menu_item('signup')
        self.login_page.check_login_to_your_account_title_is_displayed()
        self.login_page.fill_login_inputs(correct_user_email, correct_user_password)
        self.login_page.click_on_login_btn()
        self.home_page.check_user_is_logged_in(correct_user_name)
        self.login_page.click_on_nav_menu_item('logout')
        self.login_page.verify_url(login_page_url)

    def test_register_user_with_existing_email(self, test_setup):
        """Test user registration with existing email
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.home_page.verify_url(home_page_url)
        self.home_page.click_on_nav_menu_item('signup')
        self.login_page.check_new_user_signup_title_is_displayed()
        self.login_page.fill_signup_inputs(user_name, correct_user_email)
        self.login_page.click_on_signup_btn()
        self.login_page.check_signup_error_message_is_displayed()







