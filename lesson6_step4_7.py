from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select




try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.ID, 'num1').text
    x2 = browser.find_element(By.ID, 'num2').text
    y = str(str(int(x1)+int(x2)))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y) 




    browser.find_element(By.id,  "solve").click



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()