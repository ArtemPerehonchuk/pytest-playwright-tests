from playwright.sync_api import Page
from pages.home_page import HomePage
from data.test_data import TestData


class PaymentPage(HomePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.__name_of_card_input = self.page.locator('[data-qa="name-on-card"]')
        self.__card_number_input = self.page.locator('[data-qa="card-number"]')
        self.__cvc_input = self.page.locator('[data-qa="cvc"]')
        self.__month_input = self.page.locator('[data-qa="expiry-month"]')
        self.__year_input = self.page.locator('[data-qa="expiry-year"]')
        self.__pay_and_confirm_order_btn = self.page.locator('#submit')
        self.__success_message = self.page.get_by_text('Congratulations! Your order has been confirmed!')

    def fill_payment_details(self) -> None:
        payment_details = TestData.generate_input_values()
        self.__name_of_card_input.fill(payment_details["card_name"])
        self.__card_number_input.fill(payment_details["card_number"])
        self.__cvc_input.fill(payment_details["cvc_code"])
        self.__month_input.fill(payment_details["expiry_month"])
        self.__year_input.fill(str(payment_details["expiry_year"]))

    def click_on_pay_and_confirm_order_btn(self) -> None:
        self.__pay_and_confirm_order_btn.click()

    def check_success_message_is_displayed(self) -> None:
        self.__success_message.wait_for(state='visible', timeout=5000)
        assert self.__success_message.is_visible()