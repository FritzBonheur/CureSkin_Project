from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when('Click on Returns&Orders')
def click_button(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('Verify Email field is present')
def verify_email_field(context):
    context.driver.find_element(By.ID, 'ap_email')

@then('Verify elements are present for {expected_result}')
def verify_elements_are_present(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'



