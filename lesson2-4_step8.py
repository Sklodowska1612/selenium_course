from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:

    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    #price = browser.find_element(By.CSS_SELECTOR, "h5#price")
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, "12").until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"),"$100")
        )
    """"# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    button = WebDriverWait(browser, 5).until_not(
            EC.element_to_be_clickable((By.ID, "verify"))
        )"""
    button =  browser.find_element(By.CSS_SELECTOR, "#book.btn.btn-primary").click()
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)


    button1 = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button1.click()
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

