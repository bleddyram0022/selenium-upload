from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait



@pytest.(scope="class")
def setup(request):
   driver = webdriver.Chrome()
 #  wait = webdriver(driver, 10)
   driver.maximize_window()
   request.cls.driver = driver
#   request.cls.wait = wait
   yield
   driver.close()
