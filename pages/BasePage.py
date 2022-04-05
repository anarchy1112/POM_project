
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self,driver):
        self.driver=driver

    def click(self,locator):
        self.driver.find_element(By.XPATH, locator).click()

    def type(self,locator,value):
        self.driver.find_element(By.XPATH, locator).send_keys(value)


    def mouseOver(self, locator):
        elem=self.driver.find_element(By.XPATH, locator)
        action=ActionChains(self.driver)
        action.move_to_element(elem).perform()

    def clearing(self, locator):
        self.driver.find_element(By.XPATH,locator).clear()


    def textExtraction(self, locator):
        return self.driver.find_element(By.XPATH,locator).text

    def textExtraction2(self, locator):
        return self.driver.find_element(By.XPATH,locator).get_attribute("textContent")

    def wait(self,locator):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, locator)))




