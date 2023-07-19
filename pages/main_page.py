from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):

    SHOP_ALL_BTN = (By.CSS_SELECTOR, 'ul.list-menu.list-menu--inline a[href="/collections/all"]')

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')

    def click_shop_all_button(self):
        self.click(*self.SHOP_ALL_BTN)
