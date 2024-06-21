from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

def test_orangeHRM():
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    print(driver.title)

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
print(driver.title)
time.sleep(2)

        # LOGIN

#driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
#time.sleep(2)
#driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
#time.sleep(2)
#driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
#time.sleep(2)

#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
#time.sleep(2)

#links=driver.find_elements(By.TAG_NAME,"a")
#print(len(links))

#for link in links:
#    print(link.text)

computers=driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[1]/a')
desktop=driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[1]/a')
notebooks=driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[2]/a')

actions=ActionChains(driver)
time.sleep(5)
actions.move_to_element(computers).move_to_element(desktop).move_to_element(notebooks).click().perform()

