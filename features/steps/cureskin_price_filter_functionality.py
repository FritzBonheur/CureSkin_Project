from behave import given, when, then


@given("Open CureSkin Home page")
def open_browser(context):
    context.app.main_page.open_main_page()


@then("Click on Shop All section")
def click_shop_all_button(context):
    context.app.main_page.click_shop_all_button()


@then("Adjust Price Filter")
def adjust_price_filter(context):
    context.app.shop_all_page.adjust_price_filter()


@then("Verify Products Change")
def verify_products_change(context):
    context.app.shop_all_page.verify_products_change()


@when("Verify Products are within Price Filter")
def verify_products_within_price_filter(context):
    context.app.shop_all_page.verify_products_within_price_filter()