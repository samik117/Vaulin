import time
from selenium import webdriver
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")


first_name_filed = driver.find_element("xpath", "//input[@id='firstName']") # Находим поле
first_name_filed.clear() # Очищаем поле
assert first_name_filed.get_attribute("value") == "" # Проверяем, что поле пустое
first_name_filed.send_keys("Alex") # Вводим новое значение
assert "Alex" in first_name_filed.get_attribute("value") # Проверяем, что значение изменилось


# Поле Имя
last_name_filed = driver.find_element("xpath", "//input[@id='lastName']")
last_name_filed.clear()
assert last_name_filed.get_attribute("value") == ""
last_name_filed.send_keys("Vaulin")
assert "Vaulin" in last_name_filed.get_attribute("value")

# Поле Фамилия
email_filed = driver.find_element("xpath", "//input[@id='userEmail']")
email_filed.clear()
assert email_filed.get_attribute("value") == ""
email_filed.send_keys("avaulin@email.com")
assert "avaulin@email.com" in email_filed.get_attribute("value")

# Поле Гендер
gender_button = driver.find_element("xpath", "//label[@for='gender-radio-1' and text()='Male']") # Находим наш радиобаттон
gender_button.click() # Клик по найденному элементу

# Поле номер телефона
mobile_number = driver.find_element("xpath", "//input[@id='userNumber']")
mobile_number.clear()
assert mobile_number.get_attribute("value") == ""
mobile_number.send_keys("9995872277")
assert "9995872277" in mobile_number.get_attribute("value")

# Дата рождения
birth_day = driver.find_element("xpath", "//input[@id='dateOfBirthInput']")
birth_day.click()
birth_day.send_keys(Keys.CONTROL + "a") # Выделяем предыдущее значение
birth_day.send_keys("14 Aug 1990") # Вводим наше значение
birth_day.send_keys(Keys.ENTER) # Жмем Интер

# Поле предметы
subjects_filed = driver.find_element("xpath", "//input[@id='subjectsInput']")
subjects_filed.click()
assert subjects_filed.get_attribute("value") == ""
subjects_filed.send_keys("Какие-то предметы")
assert "Какие-то предметы" in subjects_filed.get_attribute("value")

# Чек боксы

# Загрузка файла
FILE_UPLOAD_FIELD = ("xpath", "//input[@id='uploadPicture']")

file_filed = driver.find_element(*FILE_UPLOAD_FIELD)
file_filed.send_keys(r"D:\Python\Team4\Vaulin\image\foto.jpeg")

# Текущий адрес
address_filed = driver.find_element("xpath", "//textarea[@id='currentAddress']")
address_filed.click()
assert address_filed.get_attribute("value") == ""
address_filed.send_keys("Галактика млечный путь, солнечная система, планета Земля")
assert "Галактика млечный путь, солнечная система, планета Земля" in address_filed.get_attribute("value")


time.sleep(5)