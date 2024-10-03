import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


LINK = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(LINK)

def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))

try:
    button_1 = browser.find_element(By.CLASS_NAME, "btn")
    time.sleep(1)
    button_1.click()

    alert = browser.switch_to.alert
    time.sleep(1)
    alert.accept()

    x = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    input_value = browser.find_element(By.XPATH, "//input[@class='form-control']")
    input_value.send_keys(calc(x))
    time.sleep(1)

    button_2 = browser.find_element(By.CLASS_NAME, "btn")
    button_2.click()

finally:
    time.sleep(5)
    browser.quit()
