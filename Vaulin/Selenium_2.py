import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

first_name_filed = driver.find_element("xpath", "//input[@id='firstName']")
first_name_filed.send_keys("Alex")

last_name_filed = driver.find_element("xpath", "//input[@id='lastName']")
last_name_filed.send_keys("Vaulin")

email_filed = driver.find_element("xpath", "//input[@id='userEmail']")
email_filed.send_keys("avaulin@email.com")






time.sleep(5)