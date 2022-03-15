import pytest
from locators.Locators import BasicInfo
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class")
def setup(request):
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver=driver
    driver.get(BasicInfo.url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
