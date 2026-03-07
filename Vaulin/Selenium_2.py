import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

first_name_filed = driver.find_element("xpath", "//input[@id='firstName']")

first_name_filed.send_keys("Alex")

time.sleep(5)