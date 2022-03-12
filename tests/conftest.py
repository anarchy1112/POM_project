from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup_module():
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get('https://www.edureka.co/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
