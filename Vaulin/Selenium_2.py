import time
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument("--headless") # или options.add_argument("--headless=new")
# options.add_argument("--incognito")
# options.add_argument("--ignore-certificate-errors")
#options.add_argument("--window-size=1920,1080")

FILE_UPLOAD_FIELD = ("xpath", "//input[@id='uploadFile']")

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/upload/download")

file_filed = driver.find_element(*FILE_UPLOAD_FIELD)
file_filed.send_keys(r"D:\Python\Team4\Vaulin\image\example.jpeg")

time.sleep(5)