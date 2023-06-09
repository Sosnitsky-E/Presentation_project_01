from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_add_prodict_successful(self):
        self.is_element_present(*ProductPageLocators.NOTICE_PRODUCT_ADD_SUCCESSFUL)
        self.should_notice_content_product_success_message()
        self.should_total_price_go_up()

    def should_notice_content_product_success_message(self):
        prod_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        expected_notice_text = f"{prod_name} has been added to your basket."
        actual_notice_text = self.browser.find_element(*ProductPageLocators.NOTICE_PRODUCT_ADD_SUCCESSFUL).text
        assert actual_notice_text == expected_notice_text, "Wrong successful notice text"

    def should_total_price_go_up(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total_prise_text = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        in_st = total_prise_text.find("£")
        in_end = in_st + 6
        total_prise = total_prise_text[in_st:in_end]
        assert total_prise == product_price, "The total price does not go up"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NOTICE_PRODUCT_ADD_SUCCESSFUL), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_element_disappeared(*ProductPageLocators.NOTICE_PRODUCT_ADD_SUCCESSFUL),\
            "Success message is not disappeared"


