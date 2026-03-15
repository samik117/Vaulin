#import time
#from selenium import webdriver

#options = webdriver.ChromeOptions()

# опции для мимикрии под человека, для обхода капчи
#options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)

## options.add_argument("--remote-debugging-port=9222") # если 3-х оказалось недостаточно

#driver = webdriver.Chrome(options=options)

#driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
#time.sleep(6)


import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, poll_frequency=1)
driver.get("https://demoqa.com/alerts")

driver.find_element("xpath", "//button[@id='alertButton']").click()

alert = driver.switch_to.alert # переключится на алерт

time.sleep(6)
