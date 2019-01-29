from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""ALL_elements_locators"""
field_search = '[name=q]'
first_result = 'div.r>a'
text_more = '#ow16 > a'
pictures = '#lb > div > a.f9UGee.q.qs.t6psHzYPBsD__highlighted'
first_picture = '[id=rg_s]>div>a:nth-child(2)'
first_picture_site = '#rg_s > div:nth-child(1) > a.iKjWAf.irc-nic.isr-rtc.a-no-hover-decoration > div.nJGrxf.FnqxG'
first_result_after_back = 'div.r>a'


"""TEST"""

def test_search():
    driver = webdriver.WebDriver('chromedriver.exe')
    driver.get("http://google.ru/")
    print(1)
    element = get_element(field_search, driver)
    element.click()
    print(2)
    element.send_keys('Selenide',Keys.ENTER)
    element = get_element(first_result, driver)
    checklink = element.get_attribute('href')
    assert "https://ru.selenide.org/" in checklink
    print(checklink + " first result is correct")
    element = get_element(text_more, driver)
    element.click()
    element = get_element(pictures, driver)
    element.click()
    print(3)
    element = get_element(first_picture_site, driver)
    checkpicture = element.text.strip()
    assert "selenide.org" in checkpicture
    print("First picture is related to Selenide site")
    driver.back()
    element = get_element(first_result_after_back, driver)
    checkfirstlinkagain = element.get_attribute('href')
    assert checkfirstlinkagain in checklink


"""MODULES"""
def tearDown(self):
    self.driver.close()

def get_element(CSS_SELECTOR, driver) -> WebElement:
    locator = (By.CSS_SELECTOR, CSS_SELECTOR)
    WebDriverWait(driver=driver, timeout=60) \
        .until(expected_conditions.
               presence_of_element_located(locator=locator))
    element = driver.find_element_by_CSS_SELECTOR(CSS_SELECTOR=CSS_SELECTOR)
    return element
