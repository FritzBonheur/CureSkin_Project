from pages.main_page import MainPage
from pages.shop_all_page import ShopAllPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.shop_all_page = ShopAllPage(self.driver)