from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


"""TEST"""

def test_search():
    driver = webdriver.WebDriver('D:\PyCharmProjects\SAP_SF\chromedriver.exe')
    driver.implicitly_wait(30)
    driver.get("http://google.ru/")
    element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.gLFyf')))
    element.click()
    element.send_keys('Selenide', Keys.ENTER)
    element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.r>a')))
    checklink = element.get_attribute('href')
    assert "https://ru.selenide.org/" in checklink
    print(checklink + " first result is correct")
    element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.Cq34nf')))
    element.click()
    element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[id=lb]>div>a')))
    element.click()
    element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[id=rg_s]>div>a:nth-child(2)')))
    checkpicture = element.text.strip()
    assert "selenide.org" in checkpicture
    print("First picture is corresponded to Selenide website")
    driver.back()
    element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.r>a')))
    checkfirstlinkagain = element.get_attribute('href')
    assert checkfirstlinkagain in checklink

"""MODULES"""

def tearDown():
    driver.close()







