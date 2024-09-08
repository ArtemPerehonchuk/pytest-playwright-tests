from playwright.sync_api import Page
from pages.home_page import HomePage


class LoginPage(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.__new_user_signup_title = self.page.get_by_text('New User Signup!')
        self.__login_to_your_account_title = self.page.get_by_text('Login to your account')
        self.__name_input = self.page.locator('[name="name"]')
        self.__email_signup_input = self.page.locator('[data-qa="signup-email"]')
        self.__signup_button = self.page.locator('button[data-qa="signup-button"]')
        self.__email_login_input = self.page.locator('[data-qa="login-email"]')
        self.__password_login_input = self.page.locator('[data-qa="login-password"]')
        self.__login_btn = self.page.locator('[data-qa="login-button"]')
        self.__login_error_message = self.page.get_by_text('Your email or password is incorrect!')
        self.__signup_error_message = self.page.get_by_text('Email Address already exist!')

    def check_new_user_signup_title_is_displayed(self) -> None:
        self.__new_user_signup_title.wait_for(state='visible')
        assert self.__new_user_signup_title.is_visible()

    def check_login_to_your_account_title_is_displayed(self) -> None:
        self.__login_to_your_account_title.wait_for(state='visible')
        assert self.__login_to_your_account_title.is_visible()

    def fill_signup_inputs(self, name: str, email: str) -> None:
        self.__name_input.fill(name)
        self.__email_signup_input.fill(email)

    def click_on_signup_btn(self) -> None:
        self.__signup_button.click()

    def fill_login_inputs(self, email, password) -> None:
        self.__email_login_input.fill(email)
        self.__password_login_input.fill(password)

    def click_on_login_btn(self) -> None:
        self.__login_btn.click()

    def check_login_error_message_is_displayed(self) -> None:
        self.__login_error_message.wait_for(state='visible')
        self.__login_error_message.is_visible()

    def check_signup_error_message_is_displayed(self) -> None:
        self.__signup_error_message.wait_for(state='visible')
        self.__signup_error_message.is_visible()