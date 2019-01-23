import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_search():
    driver = webdriver.WebDriver('chromedriver.exe')
    print(1)
    driver.get("http://google.ru/")
    element = WebDriverWait(driver=driver, timeout=60).\
            until(expected_conditions.
                presence_of_element_located((By.XPATH, '//div[@aria-label="Голосовой поиск"]/../..//input')))
    element.click()
    print(2)
    element.send_keys('Selenide',Keys.ENTER)
    element = get_element('(//h3)[1]/..', driver=driver)
    str = element.get_attribute('href')

    if str == 'https://ru.selenide.org/':
        print('GOT IT!')
    else:
        pytest.fail(f'Link"{str}" not equal "https://ru.selenide.org/')

def tearDown(self):
    self.driver.close()

def get_element(xpath, driver) -> WebElement:
    locator = (By.XPATH, xpath)
    WebDriverWait(driver=driver, timeout=60) \
        .until(expected_conditions.
               presence_of_element_located(locator=locator))
    element = driver.find_element_by_xpath(xpath=xpath)
    return element




