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
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Amazon Logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# Email field
driver.find_element(By.ID, 'ap_email')

# Continue button
driver.find_element(By.ID, 'continue')

# Need Help Link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other Issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

# *Conditions of use link
driver.find_element(By.ID, "//a[contains(@href, 'ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088')]")

# *Privacy Notice Link
driver.find_element(By.ID, "//a[contains(@href, 'ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496')]")