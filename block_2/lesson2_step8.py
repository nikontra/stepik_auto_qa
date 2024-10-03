import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import os

LINK = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(LINK)

with open("file.txt", "w") as f:
    content = f.write("Я,Сиська Николаевна, усатая дура!")

try:
    input_first_name = browser.find_element(
        By.XPATH, '//input[@placeholder="Enter first name"]')
    input_first_name.send_keys('Сисиль')

    input_last_name = browser.find_element(
        By.XPATH, '//input[@placeholder="Enter last name"]')
    input_last_name.send_keys('Третьякова')

    input_email = browser.find_element(
        By.XPATH, '//input[@placeholder="Enter email"]')
    input_email.send_keys('sisi@cat')

    input_file = browser.find_element(
        By.XPATH, '//input[@type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input_file.send_keys(file_path)

    button = browser.find_element(
        By.XPATH, '//button[contains(text(), "Submit")]')
    button.click()

finally:
    time.sleep(3)
    browser.quit()
