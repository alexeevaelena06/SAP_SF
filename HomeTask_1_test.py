from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.WebDriver('chromedriver.exe')
driver.get("http://google.ru/")
elem = WebDriverWait(driver=driver, timeout=10).\
    until(expected_conditions.
          presence_of_element_located((By.XPATH, '//div[@aria-label="Голосовой поиск"]/../..//input')))
elem.click()
elem.send_keys('Selenide',Keys.ENTER)
elem = WebDriverWait(driver=driver, timeout=20).\
    until(expected_conditions.
          presence_of_element_located((By.XPATH, '(//h3)[1]')))

str = lists1[0].getattribute("a href")
print(str)

"""image = WebDriverWait(driver=driver, timeout=10).\
    until(expected_conditions.
        presence_of_element_located((By.XPATH, '(//img)[8]')))
"""
driver.close()

