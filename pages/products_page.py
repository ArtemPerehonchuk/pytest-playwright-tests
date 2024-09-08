import random
from playwright.sync_api import Page
from pages.home_page import HomePage


class ProductsPage(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.__products_list = self.page.locator('[class="features_items"]')
        self.__first_view_product_btn = self.page.locator('a[href="/product_details/1"]')
        self.__search_input = self.page.locator('[name="search"]')
        self.__search_btn = self.page.locator('#submit_search')
        self.__searched_products_list_title = self.page.get_by_text('Searched Products')
        # self.__first_product = self.page.locator('/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]')
        # self.__first_product_add_to_cart_btn = self.page.locator('[data-product-id="1"]')
        # self.__second_product = self.page.locator('/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]')
        # self.__second_product_add_to_cart_btn = self.page.locator('[data-product-id="2"]')
        self.__continue_shopping_btn = self.page.get_by_text('Continue Shopping')
        # self.__view_cart_btn = self.page.locator('a[href="/view_cart"]')

        self.__search_word = None

    def check_products_list_is_displayed(self) -> None:
        self.__products_list.wait_for(state='visible')
        assert self.__products_list.is_visible()

    def click_on_first_view_product_btn(self) -> None:
        self.__first_view_product_btn.click()

    def get_search_word_from_products_list(self) -> str:
        product_elements = self.page.locator('.productinfo p').all()
        product_names = [element.inner_text() for element in product_elements]
        search_words = [product.split(' ') for product in product_names]
        search_word = random.choice(search_words)

        return random.choice(search_word)

    def search_product(self) -> None:
        self.__search_word = self.get_search_word_from_products_list()
        self.__search_input.fill(self.__search_word)
        self.__search_btn.click()

    def check_search_results(self) -> None:
        self.__searched_products_list_title.wait_for(state='visible')
        self.__searched_products_list_title.is_visible()

        searched_products = self.page.locator('.productinfo p').all()
        search_results =[element.inner_text() for element in searched_products]
        for result in search_results:
            assert self.__search_word in result, f"Expected '{self.__search_word}' to be in '{result}'"

    # def hover_on_product_and_click_add_to_cart_btn(self, product_name: str) -> None:
    #     if product_name.lower() == 'blue top':
    #         self.__first_product.hover()
    #         self.__first_product_add_to_cart_btn.wait_for(state='visible')
    #         self.__first_product_add_to_cart_btn.click()
    #     elif product_name.lower() == 'men tshirt':
    #         self.__second_product.hover()
    #         self.__second_product_add_to_cart_btn.wait_for(state='visible')
    #         self.__second_product_add_to_cart_btn.click()

    def click_on_continue_btn(self) -> None:
        self.__continue_shopping_btn.click()





