import pytest
from locators.Locators import BasicInfo
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def setup(request):
    if request.param=="chrome":
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif request.param=="firefox":
        driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver=driver
    driver.get(BasicInfo.url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
