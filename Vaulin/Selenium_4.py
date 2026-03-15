# Неявное ожидание
from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(7)

driver.get("https://demoqa.com/dynamic-properties")

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

driver.find_element(*VISIBLE_AFTER_BUTTON)

# Явное ожидание
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait      # Драйвер для явных ожиданий. Нужен, чтобы указать общее время ожидания для всех условий ниже
from selenium.webdriver.support import expected_conditions as EC   # Ожидаемые условия

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")
# Создаем объект(название любое)
wait = WebDriverWait(driver, 10, poll_frequency=1) # poll_frequency - частота обращения к эл-ту

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON)) # метод сам распаковывает локатор, поэтому "*" не нужна








