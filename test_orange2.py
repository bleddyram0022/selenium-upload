import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def setup():

    global driver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    driver.maximize_window()
    username =driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
    print(username.is_displayed())
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

    yield
    driver.quit()

def test_yatra():
    driver = webdriver.Chrome()
    driver.get("https://www.yatra.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()

    mousehover=driver.find_element(By.XPATH,'//*[@id="bEnginePos"]/ul/li[7]/span')
    xplore=driver.find_element(By.XPATH,'[@id="booking_engine_xplore"]/span')

    #actions=ActionChains(driver)
    ActionChains(driver).move_to_element(mousehover).move_to_element(xplore)

def test_uploadfile(setup):

    links= driver.find_elements(By.LINK_TEXT,"a")
    print(len(links))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7")
    time.sleep(2)

    #driver.switch_to.frame(0)
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div/button').click()


    #driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-attachment > div > form > div:nth-child(1) > div > div > div > div:nth-child(2) > div').send_keys("C://Program Files/Screenshot/Kodaikanal lake1.jpg")
    time.sleep(2)

def test_Admin(setup):


 # Admin EcplicitWait
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    wait=WebDriverWait(driver,10)

    username=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i')))
    username.is_displayed
    time.sleep(2)

def test_slide(setup):


 # Button Click
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/button').click()


def test_search(setup):


    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input').send_keys("Admin")
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input').click()

def test_time(setup):
    # Time
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div/input').send_keys("Linda Jane Anderson")
    time.sleep(2)
    print(driver.title)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/button').click()
    time.sleep(2)
    invalid=driver.find_element(By.XPATH,
                        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div/input').send_keys("hahaha")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/button').click()
    time.sleep(2)

    if invalid is invalid:
         print("valid is invalid")

    else:print("the invalid is invalid")

def test_inputbox(setup):


    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7")
    print(driver.current_url)

    inputbox=driver.find_elements(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
    print(len(inputbox))

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    time.sleep(1)

 #   select=Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]')).send_keys("Freelance")
  #  select.select_by_visible_text('Freelance')
   # time.sleep(2)
    #Pending
  #  select=Select(driver.find_element(By.CLASS_NAME,"oxd-icon bi-caret-down-fill oxd-select-text--arrow"))
   # select.select_by_visible_text('Freelance')

def test_link(setup):

    link =driver.find_elements(By.TAG_NAME,"a")
    print(len(link))


    for link in link:
        print(link.text)

def test_frame(setup):

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    time.sleep(2)

    driver.find_element(By.LINK_TEXT,"Leave").click()

    driver.title
    time.sleep(2)
    driver.back()
    driver.title

    driver.find_element(By.LINK_TEXT,"Admin").click()
    time.sleep(2)

    driver.forward()
    driver.title
    time.sleep(2)
    #driver.switch_to.frame("oxd-table-filter")

    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Paulpandi")
    time.sleep(5)

    driver.quit()

def test_mousehover(setup):

    print("THIS IS MOUSE HOVER ACTION")

    #driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/configurePim")

    Admin=driver.find_element(By.CSS_SELECTOR,"oxd-text oxd-text--span oxd-main-menu-item--name")
    PIM=driver.find_element(By.CSS_SELECTOR,"oxd-main-menu-item active")
    Leave=driver.find_element(By.CSS_SELECTOR,"oxd-main-menu-item")



    ActionChains(driver).move_to_element(Admin).move_to_element(PIM).move_to_element(Leave).click().perform()



#ALLEN ACADEMY WEBSITE

@pytest.fixture()
def allen():

    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.allen.ac.in/")
    driver.implicitly_wait(1)
    driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    yield
    driver.quit()

def test_alert_window_handling(allen):

    print(driver.current_url)
    driver.find_element(By.XPATH,'//*[@id="popup-kota"]/img').click()
    print(driver.current_window_handle)
    time.sleep(2)

    child= driver.window_handles

    for handle in child:
        driver.switch_to.window(handle)
        print(driver.current_url.title())

@pytest.fixture()
def HTML():

    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    driver.implicitly_wait(1)
    driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    yield
    driver.quit()


def test_HTML(HTML):

    # to traverse through the list of cell data of column 3
    rows= len(driver.find_elements(By.XPATH,'//*[@id="main"]/div[3]/div'))
    columns= len(driver.find_elements(By.XPATH,'//*[@id="main"]/div[3]/div'))

    print(rows)
    print(columns)

    #for i in l:
     #   print(i.text)



    # to close the browser
    #driver.close()






#ALLEN ACADEMY WEBSITE

@pytest.fixture()
def nopcom():

    global driver
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/computers")
    driver.implicitly_wait(1)
    driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    yield
    driver.quit()


def test_mousehover(nopcom):

    print("THIS IS MOUSE HOVER ACTION")

    #driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/configurePim")

    Computers=driver.find_element(By.CLASS_NAME,"sublist-toggle")
    Desktops =driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[1]/a')
    Software =driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[3]/a')

    time.sleep(2)

    actions= ActionChains(driver)

    actions.move_to_element(Computers).move_to_element(Desktops).move_to_element(Software ).click().perform()

@pytest.fixture()
def blogspot():

    global driver
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.implicitly_wait(1)
    driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    yield
    driver.quit()

def test_doubleside(blogspot):

    print("THIS IS MOUSE DOUBLE CLICK ACTION")

    element=driver.find_element(By.ID,"field1")
    actions = ActionChains(driver)

    actions.double_click(element).perform()






