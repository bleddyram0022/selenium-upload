import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_tui():

    global driver
    driver = webdriver.Chrome()
    driver.get("https://tus.io/demo")
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_uploadfile(test_tui):


    #driver.switch_to.frame(0)

    driver.find_element(By.XPATH,'//*[@id="P0-0"]').send_keys("C://Program Files/Screenshot/Kodaikanal lake1.jpg")
    time.sleep(2)