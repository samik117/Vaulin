import json
import os.path
import time

from cookies_manager import CookieManager
from selenium import webdriver

LOGIN_FILED = ("xpath", "//input[@id='login_email']")
PASSWORD_FILED = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")



driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")
cookies_manager = CookieManager(driver)

if os.path.exists("cookies.json"):
    cookies_manager.load()
else:
    driver.find_element(*LOGIN_FILED).send_keys("greengrass1@gmail.com")
    driver.find_element(*PASSWORD_FILED).send_keys("leGacyleGendary")
    driver.find_element(*SUBMIT_BUTTON).click()
    cookies_manager.save()
    time.sleep(10)

#print(driver.get_cookies()) # все куки
#print(driver.get_cookie("_freeconferencecall_session")) # одна конкретная

#input()

#cookies = driver.get_cookies() # переменная в которую падают куки
#with open("cookies.json", "w") as file:
    #json.dump(cookies, file, indent=4) # (что записать, куда записать, отступ)

#driver.delete_all_cookies() # удаляем старые куки

#with open("cookies.json", "r") as file:  # читаем файл с куками
    #cookies = json.load(file) # считаем инфу из файла ввиде json и положим в переменную cookies
#for cookie in cookies:
    #driver.add_cookie(cookie)

