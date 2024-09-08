from playwright.sync_api import Page, expect
from pages.home_page import HomePage


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

    def fill_payment_details(self, name_of_card, card_number, cvc, month, year) -> None:
        self.__name_of_card_input.fill(name_of_card)
        self.__card_number_input.fill(card_number)
        self.__cvc_input.fill(cvc)
        self.__month_input.fill(month)
        self.__year_input.fill(year)

    def click_on_pay_and_confirm_order_btn(self) -> None:
        self.__pay_and_confirm_order_btn.click()
        # self.page.wait_for_timeout(1000)

    def check_success_message_is_displayed(self) -> None:
        self.__success_message.wait_for(state='visible', timeout=5000)
        assert self.__success_message.is_visible()