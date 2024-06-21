import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def launchbrowser():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=chr_options))
    yield
    driver.quit()


def test_website(launchbrowser):
    driver.get("https://www.swiggy.com/")
    print(driver)