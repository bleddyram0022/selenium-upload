from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_orangeHRM():
    driver = webdriver.Chrome()
    driver.get("https://nammamadurai.in/sadmin/dashboard")
    driver.maximize_window()

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(5)

def test_loginpage():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    driver.maximize_window()
    print(driver.title)

    time.sleep(5)

def test_verifytitle():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    driver.maximize_window()
    print(driver.title)
    time.sleep(5)


    driver.get("https://www.shenll.com/careers.php")
    print(driver.title)
    time.sleep(5)

    driver.back()
    print(driver.title)
    time.sleep(5)

    driver.forward()
    print(driver.title)
    time.sleep(5)

    driver.quit()














