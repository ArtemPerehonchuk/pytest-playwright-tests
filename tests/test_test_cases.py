import pytest
from pages.home_page import HomePage
from data.test_data import TestData

test_cases_url = TestData.test_cases_url


class TestTestCases:
    @pytest.fixture
    def test_setup(self, new_page):
        self.home_page = HomePage(new_page)

    def test_test_cases(self, test_setup):
        """Proceed to test cases page
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.home_page.click_on_nav_menu_item('test cases')
        self.home_page.verify_url(test_cases_url)
