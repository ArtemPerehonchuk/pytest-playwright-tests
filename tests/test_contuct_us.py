import pytest

from data.test_data import TestData
from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage

home_page_url = 'https://automationexercise.com/'

user_name = TestData.name
user_email = TestData.email
subject = TestData.subject
message = TestData.message


class TestContactUs:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        # self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.home_page = HomePage(self.page)
        self.contact_us_page = ContactUsPage(self.page)

        self.page.goto(home_page_url, wait_until='networkidle')

    def test_contact_us_form(self, test_setup):
        """
        Test contact us form
        :param test_setup: setting up the browser and page objects
        :return:
        """
        self.home_page.verify_url(home_page_url)
        self.home_page.click_on_nav_menu_item('contact us')
        self.contact_us_page.check_get_in_touch_title_is_displayed()
        self.contact_us_page.fill_contact_us_inputs(user_name, user_email, subject, message)
        self.contact_us_page.upload_file()
        self.contact_us_page.click_on_submit_btn()
        self.contact_us_page.handle_alert_and_confirm_ok()
        self.contact_us_page.check_contact_us_success_message_is_displayed()
        self.contact_us_page.click_on_nav_menu_item('home')
        self.home_page.verify_url(home_page_url)
