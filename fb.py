import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@pytest.fixture()
def test_setup():

    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/?stype=lo&deoia=1&jlou=Afe1KjOwRpoofJ-yEq42wxwbquXRmX8Cw-0lOPr9HHKfQhlxQSWCOpf3HGAl-LGYKWNxAV46f1Ce0BwUyV6OHeZFeNhZFiaKALghiqhwTABdlA&smuh=6288&lh=Ac_fWf-aXGGnqbplqXo")
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_fb(test_setup):


    day_element= driver.find_element(By.ID,'day')
    select = Select(day_element)
    select.select_by_index(2)

    time.sleep(2)


