import os
from playwright.sync_api import Page
from pages.home_page import HomePage
from data.test_data import TestData


class ContactUsPage(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.__get_in_touch_title = self.page.get_by_text('Get In Touch')
        self.__contact_us_name_input = self.page.locator('[data-qa="name"]')
        self.__contact_us_email_input = self.page.locator('[data-qa="email"]')
        self.__contact_us_subject_input = self.page.locator('[data-qa="subject"]')
        self.__contact_us_message_input = self.page.locator('[data-qa="message"]')
        self.__choose_file_btn = self.page.locator('[name="upload_file"]')
        self._contact_us_submit_btn = self.page.locator('[data-qa="submit-button"]')
        self.__contact_us_success_message = self.page.locator('[class="status alert alert-success"]')

    def check_get_in_touch_title_is_displayed(self) -> None:
        self.__get_in_touch_title.wait_for(state='visible')
        assert self.__get_in_touch_title.is_visible()

    def fill_contact_us_inputs(self):
        input_values = TestData.generate_input_values()
        self.__contact_us_name_input.fill(input_values["name"])
        self.__contact_us_email_input.fill(input_values["email"])
        self.__contact_us_subject_input.fill(input_values["subject"])
        self.__contact_us_message_input.fill(input_values["message"])

    def upload_file(self) -> None:

        file_path = os.path.join(os.path.dirname(__file__), "..", "data", "file.txt")

        with self.page.expect_file_chooser() as fc_info:
            self.__choose_file_btn.click()

        file_chooser = fc_info.value
        file_chooser.set_files(file_path)

    def click_on_submit_btn(self) -> None:
        self._contact_us_submit_btn.click()

    def handle_alert_and_confirm_ok(self) -> None:
        self.page.on("dialog", lambda dialog: dialog.accept())

    def check_contact_us_success_message_is_displayed(self) -> None:
        self.__contact_us_success_message.is_visible()

