import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


LINK = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(LINK)

def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))

try:
    x_element= browser.find_element(By.CSS_SELECTOR, ".form-group span:nth-child(2)")
    x = x_element.text
    y = calc(x)
    input_element = browser.find_element(By.CSS_SELECTOR, ".form-group .form-control")
    input_element.send_keys(y)
    time.sleep(1)

    check_element = browser.find_element(By.CSS_SELECTOR, ".form-check .form-check-input")
    check_element.click()
    time.sleep(1)

    radio_element = browser.find_element(By.CSS_SELECTOR, '.form-check [value="robots"]')
    radio_element.click()
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()


finally:
    time.sleep(10)
    browser.quit()
