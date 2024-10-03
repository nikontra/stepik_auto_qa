from selenium import webdriver
from selenium.webdriver.common.by import By


LINK = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(LINK)

try:
    button = browser.find_element(By.ID, "button")
    button.click()

finally:
    browser.quit()
