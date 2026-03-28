import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)
driver = webdriver.Chrome(options=options)

# Переходим на сайт
driver.get("https://www.saucedemo.com")
time.sleep(0.5)

# Проверка, что открылся верный сайт
assert driver.current_url == "https://www.saucedemo.com/", "Указанный сайт не верен"
print("Сайт указан верно")

# Заполняем поле Логин
username_filed = driver.find_element("xpath", "//input[@id='user-name']")   # Находим поле
username_filed.send_keys("standard_user")                                   # Вводим значение

# Заполняем поле Пароль
password_filed = driver.find_element("xpath", "//input[@id='password']")    # Находим поле
password_filed.send_keys("secret_sauce")                                    # Вводим новое значение

# Жмем кнопку  Login
login_button = driver.find_element("xpath", "//input[@id='login-button']")  # Находим кнопку
login_button.click()                                                        # Жмем кнопку

# Проверка, что авторизация успешна и осуществлен переход на страницу товаров
assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Авторизация провалена"
print("Вы успешно авторизовались")
time.sleep(1.5)


# Добавляем товар в корзину
button_join_product_4 = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")    # Находим кнопку добавления товара
button_join_product_4.click()                                                                                   # Добавляем товар
time.sleep(0.5)

button_join_product_2 = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']")
button_join_product_2.click()
time.sleep(0.5)

button_join_product_6 = driver.find_element("xpath", "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
button_join_product_6.click()
time.sleep(0.5)

# Удаляем товар не заходя в корзину
button_remove_product_2 = driver.find_element("xpath", "//button[@id='remove-sauce-labs-bike-light']")    # Находим кнопку удаления товара
button_remove_product_2.click()                                                                           # Удаляем товар
time.sleep(0.5)

# Удаляем товар в корзине
button_basket = driver.find_element("xpath", "//a[@class='shopping_cart_link']")                                    # Находим кнопку перехода в корзину
button_basket.click()                                                                                               # Переходим в корзину
time.sleep(0.5)
assert driver.current_url == "https://www.saucedemo.com/cart.html", "Переход в корзину провален"
print("Вы успешно перешли в корзину")
button_remove_in_basket = driver.find_element("xpath", "//button[@id='remove-test.allthethings()-t-shirt-(red)']")  # Находим кнопку удаления товара
button_remove_in_basket.click()                                                                                     # Удаляем товар
time.sleep(0.5)

# Оформляем покупку
button_checkout = driver.find_element("xpath", "//button[@id='checkout']")
button_checkout.click()
time.sleep(0.5)
assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html", "Переход на страницу оформления провален"
print("Вы успешно перешли на страницу оформления")

# Заполняем данные покупателя








time.sleep(5)
