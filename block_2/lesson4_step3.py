from selenium import webdriver
from selenium.webdriver.common.by import By

import time


LINK = "http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(LINK)

try:
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    message = browser.find_element(By.ID, "verify_message").text
    assert message == "Verification was successful!"

finally:
    time.sleep(2)
    browser.quit()
