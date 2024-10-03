import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

LINK = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()

browser.get(LINK)

def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))

try:
    button_book = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    if price:
        button_book.click()

    x = browser.find_element(By.ID, "input_value").text
    input_value = browser.find_element(By.ID, "answer")
    input_value.send_keys(calc(x))

    button_submit = browser.find_element(By.ID, "solve")
    time.sleep(2)
    button_submit.click()

finally:
    time.sleep(5)
    browser.quit()

