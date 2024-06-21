from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_NMApp():
    driver = webdriver.Chrome()
    driver.get("https://mkuniversity.ac.in/dde/Notifications.php")
    driver.maximize_window()

driver = webdriver.Chrome()
driver.get("https://nammamadurai.in/sadmin/login")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(1)



driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/div/div/div[2]/div/form/div[1]/input').send_keys("sadmin@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="Password-toggle"]/a/i').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="Password-toggle"]/input').send_keys("sadmin@123")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/div/div/div[2]/div/form/div[4]/input').click()
time.sleep(1)
driver.get("https://nammamadurai.in/sadmin/dashboard")
time.sleep(1)

print(driver.title)
driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div[1]/div/div/a[1]').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div[1]/div/div/a[1]').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div[1]/div/div').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent-4"]/div/div[2]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent-4"]/div/div[2]/a/span[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent-4"]/div/div[3]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent-4"]/div/div[3]/a').click()
time.sleep(1)

def test_Introduction():

    driver = webdriver.Chrome()
driver.get("https://nammamadurai.in/sadmin/introduction")
driver.maximize_window()
print(driver.get_cookies())

driver.execute_script("window.scrollBy(0,30)","")
time.sleep(1)

def test_About_madurai():

    driver = webdriver.Chrome()
    driver.get("https://nammamadurai.in/sadmin/About")
#print(driver.is_enabled())

driver = webdriver.Chrome()
driver.get("https://nammamadurai.in/sadmin/addMultilevelCategory")

driver.find_element(By.XPATH,'//*[@id="categoryName"]').send_keys("Bus booking")
driver.find_element(By.XPATH,'//*[@id="textcolor"]').click()
driver.find_element(By.XPATH,'//*[@id="textcolor"]').click()
driver.find_element(By.XPATH,'//*[@id="textcolor"]').click()
driver.find_element(By.XPATH,'//*[@id="textcolor"]').click()
driver.find_element(By.XPATH,'//*[@id="lsImg"]').click()









