from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self,driver):
        self.driver=driver

    def click(self,locator):
        if str(locator).endswith('XPATH'):
            self.driver.find_element(By.XPATH, locator).click()
        if str(locator).endswith('CSS'):
            self.driver.find_element(By.CSS, locator).click()
        if str(locator).endswith('ID'):
            self.driver.find_element(By.ID, locator).click()

    def type(self,locator,value):
        if str(locator).endswith('XPATH'):
            self.driver.find_element(By.XPATH, locator).send_keys(value)
        if str(locator).endswith('CSS'):
            self.driver.find_element(By.CSS, locator).send_keys(value)
        if str(locator).endswith('ID'):
            self.driver.find_element(By.ID, locator).send_keys(value)


    def mouseOver(self, locator):
        if str(locator).endswith('XPATH'):
            elem=self.driver.find_element(By.XPATH, locator)
        if str(locator).endswith('CSS'):
            elem=self.driver.find_element(By.CSS, locator)
        if str(locator).endswith('ID'):
            elem=self.driver.find_element(By.ID, locator)

        action=ActionChains(self.driver)
        action.move_to_element(elem).perform()


