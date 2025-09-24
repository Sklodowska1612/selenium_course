from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x= browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    сheckbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()



    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    # ждем загрузки страницы
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()