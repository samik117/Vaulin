import allure
from allure_commons.types import Severity
from allure_commons.types import AttachmentType
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver # создай мне в классе объект драйвер
    yield
    driver.quit()


@allure.epic("HomeWork")
class TestHomeWork:
    @pytest.mark.smoke
    @allure.title("Buy clothes")
    @allure.severity(Severity.BLOCKER)
    @allure.link(url="https://confluence.com/buy_clothers", name="Documentation" )
    def test_open_page(self):

        with allure.step("Open page. Step 1"):
            self.driver.get("https://www.saucedemo.com")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 1",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Assert  page. Step 2"):
            assert self.driver.current_url.rstrip('/') == "https://www.saucedemo.com", "Указанный сайт не верен"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 2",
                attachment_type=allure.attachment_type.PNG
            )
        print("Сайт указан верно")
        time.sleep(0.5)

        # Заполняем поле Username
        with allure.step("Username filed. Step 3"):
            username_filed = self.driver.find_element("xpath", "//input[@id='user-name']")  # Находим поле Username
            username_filed.send_keys("standard_user")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 3",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(0.5)

        # Заполняем поле Пароль
        with allure.step("Password filed. Step 4"):
            password_filed = self.driver.find_element("xpath", "//input[@id='password']")   # Находим поле Password
            password_filed.send_keys("secret_sauce")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 4",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(0.5)

        # Жмем кнопку Login
        with allure.step("Login button. Step 5"):
            login_button = self.driver.find_element("xpath", "//input[@id='login-button']")  # Находим кнопку Login
            login_button.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 5",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(1)

        # Проверка, что авторизация успешна и осуществлен переход на страницу товаров
        with allure.step("Success authorization. Step 6"):
            assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Авторизация провалена"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 6",
                attachment_type=allure.attachment_type.PNG
            )
        print("Вы успешно авторизовались")
        time.sleep(1.5)

        # Добавляем товары в корзину
        with allure.step("Button join product 4. Step 7"):
            button_join_product_4 = self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")    # Находим кнопку добавления товара
            button_join_product_4.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 7",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(0.5)

        with allure.step("Button join product 2. Step 8"):
            button_join_product_2 = self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']")
            button_join_product_2.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 8",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(0.5)

        with allure.step("Button join product 6. Step 9"):
            button_join_product_6 = self.driver.find_element("xpath","//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
            button_join_product_6.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 9",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(0.5)

        # Удаляем товар в корзине
        with allure.step("Button basket. Step 10"):
            button_basket = self.driver.find_element("xpath","//a[@class='shopping_cart_link']")  # Находим кнопку перехода в корзину
            button_basket.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 10",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(0.5)
        with allure.step("Assert page. Step 11"):
            assert self.driver.current_url == "https://www.saucedemo.com/cart.html", "Переход в корзину провален"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 11",
                attachment_type=allure.attachment_type.PNG
            )
        print("Вы успешно перешли в корзину")
        with allure.step("Delete product. Step 12"):
            button_remove_in_basket = self.driver.find_element("xpath","//button[@id='remove-test.allthethings()-t-shirt-(red)']")  # Находим кнопку удаления товара
            button_remove_in_basket.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 12",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(0.5)

        # Оформляем покупку
        with allure.step("Button checkout. Step 13"):
            button_checkout = self.driver.find_element("xpath", "//button[@id='checkout']")  # Находим кнопку Checkout
            button_checkout.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 13",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(0.5)
        with allure.step("Assert page. Step 14"):
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html", "Переход на страницу оформления провален"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 14",
                attachment_type=allure.attachment_type.PNG
            )
        print("Вы успешно перешли на страницу оформления")

        # Заполняем данные покупателя
        with allure.step("Name filed. Step 15"):
            first_name_filed = self.driver.find_element("xpath", "//input[@id='first-name']")  # Находим поле Фамилия
            first_name_filed.send_keys("Кравцов")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 15",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(0.5)
        with allure.step("Last name filed. Step 16"):
            last_name_filed = self.driver.find_element("xpath", "//input[@id='last-name']")  # Находим поле Имя
            last_name_filed.send_keys("Пётр")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 16",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(0.5)
        with allure.step("Postal code. Step 17"):
            postal_code_filed = self.driver.find_element("xpath", "//input[@id='postal-code']")  # Находим поле Индекс
            postal_code_filed.send_keys("418921")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 17",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(0.5)

        # Переходим к оплате
        with allure.step("Button continue. Step 18"):
            button_continue = self.driver.find_element("xpath", "//input[@id='continue']")  # Находим кнопку Continue
            button_continue.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 18",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(0.5)
        with allure.step("Assert page. Step 19"):
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "Переход на страницу завершения покупки провален"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 19",
                attachment_type=allure.attachment_type.PNG
            )
        print("Вы успешно перешли на страницу завершения покупки")

        # Завершаем покупку
        with allure.step("Button finish. Step 20"):
            button_finish = self.driver.find_element("xpath", "//button[@id='finish']")  # Находим кнопку Finish
            button_finish.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 20",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Assert page. Step 21"):
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html", "Покупка не удалась, повторите попытку"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 21",
                attachment_type=allure.attachment_type.PNG
            )
        print("Спасибо за покупку!")

        # Возвращаемся на страницу товаров
        with allure.step("Button_back_home. Step 22"):
            button_back_home = self.driver.find_element("xpath", "//button[@id='back-to-products']")  # Находим кнопку Back Home
            button_back_home.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Step 22",
                attachment_type=allure.attachment_type.PNG
            )

        time.sleep(2)

# pytest test_HomeWork2.py --alluredir=allure-results       команда на прогон
# allure serve allure-results                               команда на отчет
# $env:STAGE="Stage-1.qa";$env:BROWSER="Chrome";$env:MR="https://google.com";$env:PYTHON="ver 3.14"; pytest test_HomeWork2.py --alluredir=allure-results описание окружения и запуск

