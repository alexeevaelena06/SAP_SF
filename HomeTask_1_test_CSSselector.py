from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""All element locators"""
# field_search = 'input.gLFyf'
# first_result = 'div.r>a'
# text_more = 'a.Cq34nf'
# pictures = '[id=lb]>div>a'
# first_picture_site = 'div.rg_bx>a:nth-child(2)'
# first_result_after_back = 'div.r>a'

dic = {
    "field_search": 'input.gLFyf',
    "first_result": 'div.r>a',
    "text_more": 'a.Cq34nf',
    "pictures": '[id=lb]>div>a',
    "first_picture_site": '[id=rg_s]>div>a:nth-child(2)',
    "first_result_after_back": 'div.r>a'
    }

"""TEST"""
def test_search():

        driver = webdriver.WebDriver('D:\PyCharmProjects\SAP_SF\chromedriver.exe')
        driver.implicitly_wait(60)
        driver.get("http://google.ru/")
        element = wait_and_get_element(driver, "field_search")
        element.click()
        element.send_keys('Selenide', Keys.ENTER)
        element = wait_and_get_element(driver, "first_result")
        checklink = element.get_attribute('href')
        assert "https://ru.selenide.org/" in checklink
        print(checklink + " first result is correct")
        element = wait_and_get_element(driver, "text_more")
        element.click()
        element = wait_and_get_element(driver, "pictures")
        element.click()
        element = wait_and_get_element(driver, "first_picture_site")
        checkpicture = element.text.strip()
        assert "selenide.org" in checkpicture
        print("First picture is corresponded to Selenide website")
        driver.back()
        element = wait_and_get_element(driver, "first_result_after_back")
        checkfirstlinkagain = element.get_attribute('href')
        assert checkfirstlinkagain in checklink


"""MODULES"""

def tearDown():
    driver.close()

def wait_and_get_element(driver, locator):
    element = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
    return element


