import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""ALL_elements_locators"""
field_search = '//div[@aria-label="Голосовой поиск"]/../..//input'
first_result = '(//h3)[1]/..'
text_more = '//*[@id="ow16"]/a'
pictures = '//*[@id="lb"]/div/a[1]'
first_picture = '//*[@id="6E5nxbsENroDNM:"]'
first_result_after_back = '(//h3)[1]/..'
first_picture_site = '//*[@id="rg_s"]/div[1]/a[2]/div[2]'

"""TEST"""

def test_search():
    driver = webdriver.WebDriver('chromedriver.exe')
    driver.get("http://google.ru/")
    element = get_element(field_search, driver)
    element.click()
    element.send_keys('Selenide',Keys.ENTER)
    element = get_element(first_result, driver)
    checklink = element.get_attribute('href')

    if checklink == 'https://ru.selenide.org/':
        print('Первая ссылка совпадает с "https://ru.selenide.org!"')
    else:
        pytest.fail(f'Link"{checklink}" not equal "https://ru.selenide.org/')
    element = get_element(text_more, driver)
    element.click()
    element = get_element(pictures, driver)
    element.click()
    element = get_element(first_picture, driver)
    checkpicture = element.get_attribute('alt')
    i = "Selenide" in checkpicture
    if i:
        print("Соотносится с Selenide")
    else:
        print("Не соотносится с Selenide")
    element = get_element(first_picture_site, driver)
    checkpicture = element.text.strip()
    i = "selenide.org" in checkpicture
    if i:
        print('Соотносится с сайтом "selenide.org"')
    else:
        print('Не соотносится с сайтом "selenide.org"')

    driver.back()
    element = get_element(first_result_after_back, driver)
    checkfirstlinkagain = element.get_attribute('href')
    if checkfirstlinkagain == checklink:
        print('Совпадают ссылки после возврата на основную страницу')
    else:
        pytest.fail(f'Link"{checkfirstlinkagain}" not equal "https://ru.selenide.org/')


"""MODULES"""
def tearDown(self):
    self.driver.close()

def get_element(xpath, driver) -> WebElement:
    locator = (By.XPATH, xpath)
    WebDriverWait(driver=driver, timeout=60) \
        .until(expected_conditions.
               presence_of_element_located(locator=locator))
    element = driver.find_element_by_xpath(xpath=xpath)
    return element




