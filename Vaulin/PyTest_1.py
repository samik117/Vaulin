from selenium import webdriver

#class TestExample:

    #def test_example(self):
        #driver = webdriver.Chrome()
        #driver.get("https://demoqa.com/login")
        #assert driver.current_url == "https://demoqa.com/login", "Открыта некорректная страница"


# Вторая часть
class TestExample:
    # Locators
    USERNAME_FIELD = ("xpath", "//input[@id='userName']")
    EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
    CURRENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='currentAddress']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    OUTPUT_BLOCK = ("xpath", "//div[@id='output']")

    # Тестовый метод
    def test_valid_data(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/text-box")

        username = driver.find_element(*self.USERNAME_FIELD)
        username.send_keys("Alex")
        assert username.get_attribute("value") == "Alex"

        email = driver.find_element(*self.EMAIL_FIELD)
        email.send_keys("mail@email.com")
        assert email.get_attribute("value") == "mail@email.com"

        address = driver.find_element(*self.CURRENT_ADDRESS_FIELD)
        address.send_keys("Stepnoi 8")
        assert address.get_attribute("value") == "Stepnoi 8"

        driver.find_element(*self.SUBMIT_BUTTON).click()

        output = driver.find_element(*self.OUTPUT_BLOCK)
        assert output.is_displayed() is True
        assert ("Alex" and "mail@email.com" and "Stepnoi 8") in output.text

# Третья часть

class TestExample:

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_open_login_page(self):
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login", "Error url"

    def teardown_method(self):
        self.driver.quit()

