# Выбор чекбокса
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")

checkbox = driver.find_element("xpath", "//span[@class='rc-tree-checkbox']")
checkbox.click()

time.sleep(5)


# Выбор радиобаттон
import time
from selenium import webdriver

YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']")
IMPRESSIVE_RADIO_BUTTON = ("xpath", "//input[@id='impressiveRadio']")
NO_RADIO_BUTTON = ("xpath", "//input[@id='noRadio']")

driver = webdriver.Chrome()
driver.get("https://demoqa.com/radio-button")

#print(driver.find_element(*NO_RADIO_BUTTON).is_enabled())  # Проверка элемента на кликабельность

driver.find_element(*YES_RADIO_BUTTON).click()

time.sleep(5)


# Выбор из выпадающего списка
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = Select(driver.find_element(*DROPDOWN_ELEMENT))

#dropdown.select_by_index(2) # выбор по индексу
#dropdown.select_by_value("1") # выбор по атрибуту
dropdown.select_by_visible_text("Option 2") # выбор по тексту

time.sleep(4)

# Мульти селект
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

select = driver.find_element(*MULTISELECT)
select.send_keys("Green")
assert select.get_atrribute("value") == "Green"
select.send_keys(Keys.ENTER)
select.send_keys(Keys.ESCAPE)

select = driver.find_element(*MULTISELECT)
select.send_keys("Red")
assert select.get_atrribute("value") == "Red"
select.send_keys(Keys.ENTER)
select.send_keys(Keys.ESCAPE)


time.sleep(4)







