from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        self.__signup_login_item = self.page.locator('[href="/login"]')
        self.__delete_account_item = self.page.get_by_text(' Delete Account')
        self.__logout_item = self.page.get_by_text(' Logout')
        self.__contact_us_item = self.page.get_by_text(' Contact us')
        self.__test_cases_item = self.page.locator('#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a')
        self.__products_item = self.page.get_by_text(' Products')
        self.__logged_in_item = self.page.get_by_text(' Logged in as ')
        self.__cart_item = self.page.locator('#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(3) > a')
        self.__home_item = self.page.get_by_text(' Home')
        self.__footer_container = self.page.locator('[class="footer-widget"]')
        self.__subscription_title = self.page.get_by_text('Subscription')
        self.__subscription_email_input = self.page.locator('#susbscribe_email')
        self.__arrow_btn = self.page.locator('#subscribe')
        self.__success_subscribe_message = self.page.get_by_text('You have been successfully subscribed!')
        self.__first_product_view_product_btn = self.page.locator('a[href="/product_details/1"]')
        self.__first_product = self.page.locator('xpath=/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]')
        self.__first_product_add_to_cart_btn = self.page.locator(".productinfo > .btn").first
        self.__second_product = self.page.locator('xpath=/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]')
        self.__second_product_add_to_cart_btn = self.page.locator('.productinfo > [data-product-id="2"]')
        self.__continue_shopping_btn = self.page.get_by_text('Continue Shopping')
        self.__view_cart_btn = self.page.get_by_role("link", name="View Cart")

    def verify_url(self, expected_url) -> None:
        current_url = self.page.url
        assert current_url == expected_url, f"Expected URL to be '{expected_url}', but got '{current_url}'"

    def click_on_nav_menu_item(self, item_name: str) -> None:
        if item_name.lower() == 'login' or item_name == 'signup':
            self.__signup_login_item.scroll_into_view_if_needed()
            self.__signup_login_item.click()
        elif item_name.lower() == 'logout':
            self.__logout_item.scroll_into_view_if_needed()
            self.__logout_item.click()
        elif item_name.lower() == 'delete account':
            self.__delete_account_item.scroll_into_view_if_needed()
            self.__delete_account_item.click()
        elif item_name.lower() == 'contact us':
            self.__contact_us_item.scroll_into_view_if_needed()
            self.__contact_us_item.click()
        elif item_name.lower() == 'test cases':
            self.__test_cases_item.scroll_into_view_if_needed()
            self.__test_cases_item.click()
        elif item_name.lower() == 'products':
            self.__products_item.scroll_into_view_if_needed()
            self.__products_item.click()
        elif item_name.lower() == 'cart':
            self.__cart_item.scroll_into_view_if_needed()
            self.__cart_item.click()
        elif item_name.lower() == 'home':
            self.__home_item.scroll_into_view_if_needed()
            self.__home_item.click()

    def check_user_is_logged_in(self, username) -> None:
        assert self.__logged_in_item.is_visible()
        expect(self.__logged_in_item).to_have_text(f'Logged in as {username}')

    def click_on_logout_item(self) -> None:
        self.__logout_item.click()

    def scroll_to_footer(self) -> None:
        self.__footer_container.scroll_into_view_if_needed()

    def check_subscription_title_is_displayed(self) -> None:
        assert self.__subscription_title.is_visible()

    def fill_subscription_email_input(self, email) -> None:
        self.__subscription_email_input.fill(email)

    def click_on_arrow_btn(self) -> None:
        self.__arrow_btn.click()

    def check_success_subscribe_message_is_displayed(self) -> None:
        self.__success_subscribe_message.wait_for(state='visible')
        self.__success_subscribe_message.is_visible()

    def click_on_first_view_product_btn(self) -> None:
        self.__first_product_view_product_btn.click()

    def hover_on_product_and_click_add_to_cart_btn(self, product_name: str) -> None:
        if product_name.lower() == 'blue top':
            self.__first_product.scroll_into_view_if_needed()
            self.__first_product.hover()
            self.__first_product_add_to_cart_btn.wait_for(state='visible')
            self.__first_product_add_to_cart_btn.click()
        elif product_name.lower() == 'men tshirt':
            self.__first_product.scroll_into_view_if_needed()
            self.__second_product.hover()
            self.__second_product_add_to_cart_btn.wait_for(state='visible')
            self.__second_product_add_to_cart_btn.click()

    def click_on_continue_btn(self) -> None:
        self.__continue_shopping_btn.click()

    def click_on_view_cart_btn(self) -> None:
        self.__view_cart_btn.click()






