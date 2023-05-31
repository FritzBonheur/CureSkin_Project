from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Returns&Orders')
def click_button(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify elements are present for {expected_results}')
def verify_elements_are_present(context, expected_result):
    actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'

