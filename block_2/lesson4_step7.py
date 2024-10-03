from selenium import webdriver
from selenium.webdriver.common.by import By


LINK = "http://suninjuly.github.io/wait2.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(LINK)

try:
    button = browser.find_element(By.ID, "verify']")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    browser.quit()
