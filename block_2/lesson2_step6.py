import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(LINK)

def calc(a):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    x = browser.find_element(By.ID, "input_value").text
    input_value = browser.find_element(By.ID, "answer")
    input_value.send_keys(calc(x))

    button = browser.find_element(By.TAG_NAME, "button")
    button.location_once_scrolled_into_view

    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button.click()

finally:
    time.sleep(5)
    browser.quit()
