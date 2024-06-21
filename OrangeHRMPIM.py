import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.fixture()
def orange():

    global driver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    driver.maximize_window()
    print(driver.title)


def test_login(orange):
        # LOGIN
    driver.find_element(By.NAME,"username").send_keys("Admin")
    #print(len(inbutbox))
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)


def test_mouse(orange):

    print("THIS IS MOUSE HOVER ACTION")

    #driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/configurePim")

    Admin=driver.find_element(By.LINK_TEXT,"oxd-text oxd-text--span oxd-main-menu-item--name")
    PIM=driver.find_element(By.LINK_TEXT,"oxd-main-menu-item active")
    Leave=driver.find_element(By.LINK_TEXT,"oxd-main-menu-item")

    actions=ActionChains(driver)

    actions.move_to_element(Admin).move_to_element(PIM).move_to_element(Leave).click().perform()


