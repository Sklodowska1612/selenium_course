from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import os



try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
    input3 = browser.find_element(By.NAME, "email").send_keys("Ivanovich")
    element = browser.find_element(By.CSS_SELECTOR, "#file")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    # ждем загрузки страницы
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()