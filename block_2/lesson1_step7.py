from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math


LINK = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(LINK)

def calc(a:str):
    return str(math.log(abs(12*math.sin(int(a)))))

try:
    img = browser.find_element(By.TAG_NAME, "img")
    value = img.get_attribute("valuex")
    input_el = browser.find_element(By.ID, "answer")
    input_el.send_keys(calc(value))
    time.sleep(1)

    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    time.sleep(1)

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    time.sleep(1)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()


finally:
    time.sleep(5)
    browser.quit()
