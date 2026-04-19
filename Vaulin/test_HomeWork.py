import time
import pytest
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
class TestHomeWork:
    @pytest.mark.usefixtures("driver")
    def test_open_page(self):

        self.driver.get("https://www.saucedemo.com")
        assert self.driver.current_url == "https://www.saucedemo.com/", "Указанный сайт не верен"
        print("Сайт указан верно")
        time.sleep(0.5)

# Заполняем поле Username
        username_filed = self.driver.find_element("xpath", "//input[@id='user-name']")   # Находим поле Username
        username_filed.send_keys("standard_user")
        time.sleep(0.5)

# Заполняем поле Пароль
        password_filed = self.driver.find_element("xpath", "//input[@id='password']")    # Находим поле Password
        password_filed.send_keys("secret_sauce")
        time.sleep(0.5)

# Жмем кнопку  Login
        login_button = self.driver.find_element("xpath", "//input[@id='login-button']")  # Находим кнопку Login
        login_button.click()

# Проверка, что авторизация успешна и осуществлен переход на страницу товаров
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Авторизация провалена"
        print("Вы успешно авторизовались")
        time.sleep(1.5)

# Добавляем товар в корзину
        button_join_product_4 = self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")    # Находим кнопку добавления товара
        button_join_product_4.click()
        time.sleep(0.5)

        button_join_product_2 = self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']")
        button_join_product_2.click()
        time.sleep(0.5)

        button_join_product_6 = self.driver.find_element("xpath","//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
        button_join_product_6.click()
        time.sleep(0.5)
