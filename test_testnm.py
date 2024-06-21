import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test_NMApp():
    driver = webdriver.Chrome()
    driver.get("https://mkuniversity.ac.in/dde/Notifications.php")
    driver.maximize_window()


driver= webdriver.Chrome()
driver.get("https://nammamadurai.in/sadmin/login")
driver.maximize_window()
time.sleep(1)

# Sadmin login

driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/div/div/div[2]/div/form/div[1]/input').send_keys("sadmin@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="Password-toggle"]/a/i').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="Password-toggle"]/input').send_keys("sadmin@123")
time.sleep(1)


driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/div/div/div[2]/div/form/div[4]/input').click()
time.sleep(1)
driver.get("https://nammamadurai.in/sadmin/dashboard")
time.sleep(2)
inputboxes= driver.find_element(By.CLASS_NAME,"form-control").is_displayed()
print(inputboxes)
inputboxes= driver.find_element(By.CLASS_NAME,"form-control").is_enabled()
print(inputboxes)
inputboxes= driver.find_element(By.CLASS_NAME,"form-control").is_selected()
print(inputboxes)

driver.get("https://nammamadurai.in/sadmin/dashboard")
time.sleep(1)

links=driver.find_element(By.TAG_NAME,"a")
print(links)

print("number of links in present:")

if links.is_displayed():
    print("Links working good")

else: print("links not working")



