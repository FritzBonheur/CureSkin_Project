from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# open the url
driver.get('https://www.amazon.com/')

# Amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# Create account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Your name field
driver.find_element(By.CSS_SELECTOR, '.a-input-text.a-span12.auth-autofocus.auth-required-field')

# Email field
driver.find_element(By.CSS_SELECTOR, '#ap_email')

# Password field
driver.find_element(By.CSS_SELECTOR, '#ap_password')

# Re-enter password field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# Create your account button
driver.find_element(By.CSS_SELECTOR, '#continue')

# Conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

# Privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

# Sign in
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?']")