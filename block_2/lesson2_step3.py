from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from selenium.webdriver.support.select import Select

LINK = "https://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(LINK)

try:
    x_element = browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(2)").text
    y_element = browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(4)").text

    sum = int(x_element) + int(y_element)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(sum))

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()


finally:
    time.sleep(4)
    browser.quit()
