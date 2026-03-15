# Неявное ожидание
from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(7)

driver.get("https://demoqa.com/dynamic-properties")

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

driver.find_element(*VISIBLE_AFTER_BUTTON)
