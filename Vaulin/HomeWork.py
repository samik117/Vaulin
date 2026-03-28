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

# Заполняем поле Username
username_filed = driver.find_element("xpath", "//input[@id='user-name']")   # Находим поле Username
username_filed.send_keys("standard_user")
time.sleep(0.5)

# Заполняем поле Пароль
password_filed = driver.find_element("xpath", "//input[@id='password']")    # Находим поле Password
password_filed.send_keys("secret_sauce")
time.sleep(0.5)

# Жмем кнопку  Login
login_button = driver.find_element("xpath", "//input[@id='login-button']")  # Находим кнопку Login
login_button.click()

# Проверка, что авторизация успешна и осуществлен переход на страницу товаров
assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Авторизация провалена"
print("Вы успешно авторизовались")
time.sleep(1.5)


# Добавляем товар в корзину
button_join_product_4 = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")    # Находим кнопку добавления товара
button_join_product_4.click()
time.sleep(0.5)

button_join_product_2 = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']")
button_join_product_2.click()
time.sleep(0.5)

button_join_product_6 = driver.find_element("xpath", "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
button_join_product_6.click()
time.sleep(0.5)

# Удаляем товар не заходя в корзину
button_remove_product_2 = driver.find_element("xpath", "//button[@id='remove-sauce-labs-bike-light']")    # Находим кнопку удаления товара
button_remove_product_2.click()
time.sleep(0.5)

# Удаляем товар в корзине
button_basket = driver.find_element("xpath", "//a[@class='shopping_cart_link']")                                    # Находим кнопку перехода в корзину
button_basket.click()
time.sleep(0.5)
assert driver.current_url == "https://www.saucedemo.com/cart.html", "Переход в корзину провален"
print("Вы успешно перешли в корзину")
button_remove_in_basket = driver.find_element("xpath", "//button[@id='remove-test.allthethings()-t-shirt-(red)']")  # Находим кнопку удаления товара
button_remove_in_basket.click()
time.sleep(0.5)

# Оформляем покупку
button_checkout = driver.find_element("xpath", "//button[@id='checkout']")      # Находим кнопку Checkout
button_checkout.click()
time.sleep(0.5)
assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html", "Переход на страницу оформления провален"
print("Вы успешно перешли на страницу оформления")

# Заполняем данные покупателя
first_name_filed = driver.find_element("xpath", "//input[@id='first-name']")    # Находим поле Фамилия
first_name_filed.send_keys("Кравцов")
time.sleep(0.5)
last_name_filed = driver.find_element("xpath", "//input[@id='last-name']")      # Находим поле Имя
last_name_filed.send_keys("Пётр")
time.sleep(0.5)
postal_code_filed = driver.find_element("xpath", "//input[@id='postal-code']")  # Находим поле Индекс
postal_code_filed.send_keys("418921")
time.sleep(0.5)

# Переходим к оплате
button_continue = driver.find_element("xpath", "//input[@id='continue']")  # Находим кнопку Continue
button_continue.click()
time.sleep(0.5)
assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "Переход на страницу завершения покупки провален"
print("Вы успешно перешли на страницу завершения покупки")

# Завершаем покупку
button_finish = driver.find_element("xpath", "//button[@id='finish']")  # Находим кнопку Finish
button_finish.click()
assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html", "Покупка не удалась, повторите попытку"
print("Спасибо за покупку!")

# Возвращаемся на страницу товаров
button_back_home = driver.find_element("xpath", "//button[@id='back-to-products']")  # Находим кнопку Back Home
button_back_home.click()

time.sleep(5)
