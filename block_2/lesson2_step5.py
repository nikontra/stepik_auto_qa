import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
LINK = "https://SunInJuly.github.io/execute_script.html"
browser.get(LINK)


try:
    button = browser.find_element(By.TAG_NAME, "button")
    time.sleep(1)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.location_once_scrolled_into_view
    button.click()

finally:
    time.sleep(2)
    browser.quit()
