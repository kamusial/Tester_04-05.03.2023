from selenium import webdriver
from selenium_OOP import LoginPage
import time

driver = webdriver.Chrome()
page = LoginPage(driver)
page.open()
page.enter_username('standard_user')
page.enter_password('secret_sauce')
page.click_login()
time.sleep(2)
