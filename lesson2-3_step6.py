from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, 'button.trollface.btn.btn-primary')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)


    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    # ждем загрузки страницы
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()