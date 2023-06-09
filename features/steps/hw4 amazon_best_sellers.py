from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click best sellers button')
def click_bestsellers(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]").click()


@then('Verify links are present')
def verify_links(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, 'ref=zg_bs_tab')]")
