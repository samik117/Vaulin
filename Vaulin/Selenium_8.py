
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")
wait = WebDriverWait(driver, 10, poll_frequency=1)
action = ActionChains(driver)

DOUBLE_CLICK_BUTTON = ("xpath", "//button[@id='doubleClickBtn']")
RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClickBtn']")
LEFT_CLICK_BUTTON = ("xpath", "//button[@id='DnSsn']")

#BUTTON = driver.find_element(*DOUBLE_CLICK_BUTTON)
#BUTTON = driver.find_element(*RIGHT_CLICK_BUTTON)
BUTTON = driver.find_element(*LEFT_CLICK_BUTTON)

#action.double_click(BUTTON).perform() #Двойной клик
#action.context_click(BUTTON).perform() #Правый клик
action.click(BUTTON).perform() #Левый клик

time.sleep(5)

# Вторая часть
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demoqa.com/menu")
wait = WebDriverWait(driver, 10, poll_frequency=1)
action = ActionChains(driver)

SET_1_LOCATOR = ("xpath", "//a[text()='']")
SET_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
SET_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

SET_1 = driver.find_element(*SET_1_LOCATOR)
SET_2 = driver.find_element(*SET_2_LOCATOR)
SET_3 = driver.find_element(*SET_3_LOCATOR)

action.move_to_element(SET_1).move_to_element(SET_2).move_to_element(SET_3).perform()

time.sleep(5)
