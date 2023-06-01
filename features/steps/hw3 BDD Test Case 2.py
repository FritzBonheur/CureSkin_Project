from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Cart')
def click_button(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite').click()


@then('Verify elements are preset for {expected_result}')
def verify_cart_is_empty(context, expected_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'
