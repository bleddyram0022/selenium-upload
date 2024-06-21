from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest

class TestHRM():

 def test_orangeHRM(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(self.driver.current_url)
    self.driver.implicitly_wait(10)
    self.driver.maximize_window()



  def test_login(self):
     self.driver = webdriver.Chrome()
     self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
     self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
     self.time.sleep(2)
     self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
     self.time.sleep(2)
     self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
     self.time.sleep(2)

#Button Click
self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
selftime.sleep(2)
selfdriver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/button').click()
selftime.sleep(2)
selfdriver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/button').click()

#Search
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input').send_keys("Admin")
time.sleep(2)




   #ADD  ADMIN
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
time.sleep(2)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').send_keys("Bala")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys("Paulpandi")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("Bala*12$")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Bala*12$")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
time.sleep(5)

driver.quit()

   #Admin Search
driver.find_element(By.CLASS_NAME,"oxd-main-menu-item active").click()
time.sleep(2)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"oxd-icon bi-caret-down-fill").click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Paulpandi")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input').send_keys("Bala")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space").click()
time.sleep(2)
