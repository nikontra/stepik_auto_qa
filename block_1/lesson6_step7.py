from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

letters = string.ascii_letters

LINK = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()
browser.get(LINK)

try:
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys(''.join(random.choice(letters) for _ in range(10)))
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
