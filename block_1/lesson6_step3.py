import time

from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = 'http://suninjuly.github.io/simple_form_find_task.html'
browser = webdriver.Chrome()
browser.get(LINK)


try:
    button = browser.find_element(By.ID, 'submit_button')
    time.sleep(3)
    button.click()
    time.sleep(3)
finally:
    browser.quit()
