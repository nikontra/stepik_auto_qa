from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

LINK = "http://suninjuly.github.io/find_link_text"
VALUE = str(math.ceil(math.pow(math.pi, math.e)*10000))

browser = webdriver.Chrome()
browser.get(LINK)
time.sleep(5)

try:
    link = browser.find_element(By.LINK_TEXT, VALUE)
    link.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
