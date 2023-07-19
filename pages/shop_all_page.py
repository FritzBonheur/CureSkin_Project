from pages.base_page import Page
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


class ShopAllPage(Page):
    LOWER = (By.XPATH, "//div[@class='price-range__thumbs is-lower']")
    UPPER = (By.XPATH, "//div[@class='price-range__thumbs is-upper']")
    PRODUCT = (By.XPATH, "//a[contains(text(), 'Vitamin ABC Cream')]")
    def adjust_price_filter(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.wait_for_element_appear(*self.LOWER)) \
            .move_by_offset(155, 0) \
            .release() \
            .perform()
        sleep(5)

        action = ActionChains(self.driver)
        action.click_and_hold(self.wait_for_element_appear(*self.UPPER)) \
            .move_by_offset(-20, 0) \
            .release() \
            .perform()
        sleep(5)

    def verify_products_change(self):
        self.find_element(*self.PRODUCT)


    def verify_products_within_price_filter(self):
        self.find_element()
