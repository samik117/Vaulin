import time
from selenium import webdriver

options = webdriver.ChromeOptions()

# опции для мимикрии под человека, для обхода капчи
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# options.add_argument("--remote-debugging-port=9222") # если 3-х оказалось недостаточно

driver = webdriver.Chrome(options=options)

driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
time.sleep(6)

