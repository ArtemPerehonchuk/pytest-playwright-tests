import pytest

from data.test_data import TestData
from pages.contact_us_page import ContactUsPage

home_page_url = TestData.home_page_url


class TestContactUs:
    @pytest.fixture
    def test_setup(self, new_page):
        self.contact_us_page = ContactUsPage(new_page)

    def test_contact_us_form(self, test_setup):
        """
        Test contact us form
        :param test_setup: setting up the browser and page objects
        :return:
        """
        self.contact_us_page.click_on_nav_menu_item('contact us')
        self.contact_us_page.check_get_in_touch_title_is_displayed()
        self.contact_us_page.fill_contact_us_inputs()
        self.contact_us_page.upload_file()
        self.contact_us_page.click_on_submit_btn()
        self.contact_us_page.handle_alert_and_confirm_ok()
        self.contact_us_page.check_contact_us_success_message_is_displayed()
        self.contact_us_page.click_on_nav_menu_item('home')
        self.contact_us_page.verify_url(home_page_url)
