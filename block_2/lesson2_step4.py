import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https:/google.com')

try:
    browser.execute_script("document.title='Сиська тоже';")
    time.sleep(2)
    browser.execute_script("alert('Тишка дура');")

finally:
    time.sleep(5)
    browser.quit()
