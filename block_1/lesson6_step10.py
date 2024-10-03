from selenium import webdriver
from selenium.webdriver.common.by import By
import time

LINK = "https://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(LINK)

try:
    input_1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input_1.send_keys('Тишка')
    input_2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input_2.send_keys('Петровна')
    input_3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input_3.send_keys('tishka@cat')
    time.sleep(2)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    time.sleep(1)
    welcome = browser.find_element(By.TAG_NAME, "h1")

    assert welcome.text == "Congratulations! You have successfully registered!"

finally:
    time.sleep(5)
    browser.quit()
