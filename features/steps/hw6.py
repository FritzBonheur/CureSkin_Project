from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PN_LINK = (By.XPATH, "//a[contains(@class, 'help-display-cond') and text()='Privacy Notice']")
@given ('Open Amazon T&C page')
def open_amazon_tc(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=GLSBYFE9MGKKQXXM')


@when ('Store original windows')
def store_original_window(context):
        context.original_window = context.driver.current_window_handle
        print('original:', context.original_window)
        print('All windows:', context.driver.window_handles)


@when ('Click on Amazon Privacy Notice link')
def click_link(context):
    context.driver.find_element(*PN_LINK).click()


@when ('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    print('After window opened, all windows:', all_windows)
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display'))


@then('User can close new window')
def close_new_window(context):
    context.driver.close()
    all_windows = context.driver.window_handles
    print('After window opened, all windows:', all_windows)


@then('Switch back to original window')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)
