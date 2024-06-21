import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@allure.severity(allure.severity_level.MINOR)
def test_NMApp():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(5)
#status=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').is_displayed()


#if status is True:
#    assert True

#else: status is False

@allure.severity(allure.severity_level.CRITICAL)
def test_App():
    # Button Click
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    time.sleep(2)
    print(driver.title)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/button').click()
    button=    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/button').is_selected()


    if button is True:
        print("this is button is selected")
    else: "This is not selected", allure.attach(driver.get_screenshot_as_png(), name= "test_App",attachment_type=AttachmentType.PNG)

def test_search():
    # Search
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")
    time.sleep(2)
    print(driver.title)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input').send_keys("Time")
    time.sleep(2)



    # Time:
def test_Time():
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div/input').send_keys(
        "Linda Jane Anderson")
    time.sleep(2)
    print(driver.title)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/button').click()
    time.sleep(2)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewTimesheet/employeeId/5")
    time.sleep(2)

