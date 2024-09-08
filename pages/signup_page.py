import random
import time
from playwright.sync_api import Page
from pages.home_page import HomePage


class SignupPage(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.__enter_account_info_title = self.page.get_by_text('Enter Account Information')
        self.__signup_name_input = self.page.locator('[data-qa="name"]')
        self.__signup_email_input = self.page.locator('#email')
        self.__signup_password_input = self.page.locator('[data-qa="password"]')
        self.__days_drop_down = self.page.locator('[data-qa="days"]')
        self.__months_drop_down = self.page.locator('[data-qa="months"]')
        self.__years_drop_down = self.page.locator('[data-qa="years"]')
        self.__newsletter_checkbox = self.page.locator('[name="newsletter"]')
        self.__special_offers_checkbox = self.page.locator('[name="optin"]')
        self.__signup_first_name_input = self.page.locator('[data-qa="first_name"]')
        self.__signup_last_name_input = self.page.locator('[data-qa="last_name"]')
        self.__signup_company_input = self.page.locator('[data-qa="company"]')
        self.__signup_address_input = self.page.locator('[data-qa="address"]')
        self.__signup_address2_input = self.page.locator('[data-qa="address2"]')
        self.__signup_country_drop_down = self.page.locator('[data-qa="country"]')
        self.__signup_state_input = self.page.locator('[data-qa="state"]')
        self.__signup_city_input = self.page.locator('[data-qa="city"]')
        self.__signup_zipcode_input = self.page.locator('[data-qa="zipcode"]')
        self.__signup_mobile_number_input = self.page.locator('[data-qa="mobile_number"]')
        self.__create_account_btn = self.page.locator('[data-qa="create-account"]')

    def check_enter_account_info_title_is_displayed(self) -> None:
        self.__enter_account_info_title.wait_for(state='visible')
        assert self.__enter_account_info_title.is_visible()

    def check_title_radio_btn(self, radio_btn_name) -> None:
        title_radio_btn = self.page.locator(f'input[value="{radio_btn_name}"]')
        title_radio_btn.check()

    def fill_signup_inputs(self, password) -> None:
        self.__signup_password_input.wait_for(state='visible')
        self.__signup_password_input.fill(password)

    def select_day_from_days_drop_down(self) -> None:
        self.__days_drop_down.scroll_into_view_if_needed()

        options = self.__days_drop_down.locator('option').all()
        values = [option.get_attribute('value') for option in options if option.get_attribute('value')]
        random_day = random.choice(values)

        self.__days_drop_down.select_option(random_day)

    def select_month_from_months_drop_down(self) -> None:
        self.__months_drop_down.scroll_into_view_if_needed()
        options = self.__months_drop_down.locator('option').all()
        values = [option.get_attribute('value') for option in options if option.get_attribute('value')]
        random_month = random.choice(values)

        self.__months_drop_down.select_option(random_month)

    def select_year_from_years_drop_down(self) -> None:
        self.__years_drop_down.scroll_into_view_if_needed()
        options = self.__years_drop_down.locator('option').all()
        values = [option.get_attribute('value') for option in options if option.get_attribute('value')]
        random_year = random.choice(values)

        self.__years_drop_down.select_option(random_year)

    def check_newsletter_checkbox(self) -> None:
        self.__newsletter_checkbox.scroll_into_view_if_needed()
        self.__newsletter_checkbox.check()

    def check_special_offers_checkbox(self) -> None:
        self.__special_offers_checkbox.scroll_into_view_if_needed()
        self.__special_offers_checkbox.check()

    def fill_additional_signup_inputs(self, first_name, last_name, company, address, address2, state, city, zipcode, mobile_number):
        self.__signup_first_name_input.scroll_into_view_if_needed()
        self.__signup_first_name_input.fill(first_name)
        self.__signup_last_name_input.scroll_into_view_if_needed()
        self.__signup_last_name_input.fill(last_name)
        self.__signup_company_input.scroll_into_view_if_needed()
        self.__signup_company_input.fill(company)
        self.__signup_address_input.scroll_into_view_if_needed()
        self.__signup_address_input.fill(address)
        self.__signup_address2_input.scroll_into_view_if_needed()
        self.__signup_address2_input.fill(address2)
        self.__signup_state_input.scroll_into_view_if_needed()
        self.__signup_state_input.fill(state)
        self.__signup_city_input.scroll_into_view_if_needed()
        self.__signup_city_input.fill(city)
        self.__signup_zipcode_input.scroll_into_view_if_needed()
        self.__signup_zipcode_input.fill(zipcode)
        self.__signup_mobile_number_input.scroll_into_view_if_needed()
        self.__signup_mobile_number_input.fill(mobile_number)

    def select_country_from_countries_drop_down(self) -> None:

        options = self.__signup_country_drop_down.locator('option').all()
        values = [option.get_attribute('value') for option in options if option.get_attribute('value')]
        random_country = random.choice(values)

        self.__signup_country_drop_down.select_option(random_country)

    def click_on_create_account_btn(self) -> None:
        self.__create_account_btn.click()



