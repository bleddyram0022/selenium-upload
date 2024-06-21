import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait



@pytest.mark.usefixtures("setup")
class TestOrangeHRM():

    def test_orangeHRM(self):
     self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    def test_login(self):

     print(self.driver.current_url)
     time.sleep(2)
     self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
     self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
     self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
#     input_box = self.driver.find_element(By.CLASS_NAME,"oxd-input oxd-input--active").is_displayed()

#     print(len(input_box))
     self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
     time.sleep(2)
     self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input').send_keys("Admin")
     time.sleep(2)
     self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input').click()

     self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")


    def test_search(self):
     self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")



    def test_slide(self):
     # Button Click
     self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")


     self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/button').click()
     time.sleep(2)
     self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/button').click()
     time.sleep(2)


