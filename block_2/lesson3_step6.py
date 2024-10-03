from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math


LINK = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(LINK)

def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))

try:
    button = browser.find_element(By.CLASS_NAME, "btn")
    time.sleep(2)
    button.click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    input_value = browser.find_element(By.XPATH, "//input[@id='answer']")
    time.sleep(1)
    input_value.send_keys(calc(x))
    time.sleep(1)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
