


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()

dropdown = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]')
dropdown.click()


options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='listbox']/div"))
)

if options:
    # options 0 = Select, 1 = Single, 2 = Married, 3 = Others
    first_option = options[3]
    first_option.click()

time.sleep(2)





for i in range(1,6):
        print(i)
