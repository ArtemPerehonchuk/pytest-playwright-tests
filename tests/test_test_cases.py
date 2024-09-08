import  pytest

from pages.home_page import HomePage

home_page_url = 'https://automationexercise.com/'
test_cases_url = 'https://automationexercise.com/test_cases'


class TestTestCases:
    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.home_page = HomePage(self.page)
        self.page.goto(home_page_url, wait_until='networkidle')

    def test_test_cases(self, test_setup):
        """Proceed to test cases page
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.home_page.verify_url(home_page_url)
        self.home_page.click_on_nav_menu_item('test cases')
        self.home_page.verify_url(test_cases_url)
