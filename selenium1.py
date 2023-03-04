from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://google.com')
print('Nazwa strony',driver.title)
time.sleep(2)
button1_accept = driver.find_element('id','L2AGLb')
button1_accept.click()
print(button1_accept)
search_field = driver.find_element('name','q')
search_field.send_keys('Czy jutro jest niedziela handowa?')
#search_field.send_keys(Keys.ENTER)
search_button = driver.find_element('name', 'btnK')
search_button.submit()
time.sleep(2)
driver.quit()