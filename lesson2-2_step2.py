from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, "#num1").text) + int(browser.find_element(By.CSS_SELECTOR, "#num2").text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x))  # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
    # ждем загрузки страницы
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
