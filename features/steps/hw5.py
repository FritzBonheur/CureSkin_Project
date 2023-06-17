from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product page B07BJKRR25')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


@then('Verify user can click different Slim-Fit Stretch Jean colors')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Blue, Over Dye', 'Bright White']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS) # => [WebElement1, WebElement2, WebElement3]

    for color in colors[:3]:
        color.click() # WebElement1.click(), then WebElement2.click(), then WebElement3.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]

    assert expected_colors == actual_colors, \
    f'Expected colors {expected_colors} did not match actual {actual_colors}'