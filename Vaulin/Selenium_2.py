import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")


first_name_filed = driver.find_element("xpath", "//input[@id='firstName']") # Находим поле
first_name_filed.clear() # Очищаем поле
assert first_name_filed.get_attribute("value") == "" # Проверяем, что поле пустое
first_name_filed.send_keys("Alex") # Вводим новое значение
assert "Alex" in first_name_filed.get_attribute("value") # Проверяем, что значение изменилось



last_name_filed = driver.find_element("xpath", "//input[@id='lastName']")
last_name_filed.clear()
assert last_name_filed.get_attribute("value") == ""
last_name_filed.send_keys("Vaulin")
assert "Vaulin" in last_name_filed.get_attribute("value")


email_filed = driver.find_element("xpath", "//input[@id='userEmail']")
email_filed.clear()
assert email_filed.get_attribute("value") == ""
email_filed.send_keys("avaulin@email.com")
assert "avaulin@email.com" in email_filed.get_attribute("value")

gender_button = driver.find_element("xpath", "//label[@for='gender-radio-1' and text()='Male']") # Находим наш радиобаттон
gender_button.click() # Клик по найденному элементу














time.sleep(5)