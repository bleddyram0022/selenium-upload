import email
import time
import allure
import pytest
import keyword
import frame
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException

@pytest.fixture()
def yop():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://yopmail.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login"]').send_keys("dopietesting13")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="refreshbut"]/button').click()

                 #Register different scenarios
                 #Valid user gamil and valid password
@pytest.fixture()
def dop():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://dopamineexch.wealwindemo.com/")
    current_url = driver.current_url
    print("current url:", current_url)
    #driver.implicitly_wait(5)                            # CryptoWebsite
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="navbarTogglerDemo03"]/ul/li[4]/div/div/button[2]').click()
    yield
    driver.close()
    # Valid user gamil and valid password
def test_register(dop):

    driver.get("https://dopamineexch.wealwindemo.com/signup")
    time.sleep(2)
    current_url = driver.current_url
    print("current url:", current_url)

    elements = driver.find_elements(By.TAG_NAME, "a")
    links = [element.get_attribute("href") for element in elements]

    for link in links:
     print("Number of Links Presents:", len(link))

    try:
        header = driver.find_element(By.TAG_NAME,"h2")
        assert header.is_displayed(), "Page header not found"
        print("Page header found:", header.text)

    except NoSuchElementException:
        print("Page header not found")

    driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("dopietesting13@yopmail.com")
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("Tester@123")
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/main/div/div/div[2]/div/div/div/div/form/div[2]/div/span').click()
    driver.execute_script("window.scrollBy(0,400)","")
    driver.find_element(By.XPATH,'//*[@id="confirmPassword"]').send_keys("Tester@123")
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/main/div/div/div[2]/div/div/div/div/form/div[4]/div[1]/input').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#__next > div:nth-child(2) > main > div > div > div.Common_authentication__MicOT > div > div > div > div > form > div.mt-4 > button").click()
    time.sleep(2)

def test_yopmail_activate(yop):

        driver.get("https://yopmail.com/en/wm")
        time.sleep(5)
        #driver.find_element(By.TAG_NAME,"td")
        links = driver.find_elements(By.TAG_NAME,"a")
        print(len(links))

        #driver.switch_to.frame(By.XPATH, '//iframe[@id="ifmail"]')
        #element = WebDriverWait(driver, 10).until(
        #    EC.visibility_of_all_elements_located((By.XPATH, '/html/body/main/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/p[4]/a'))
        #)

        driver.refresh()
        click_link = driver.find_element(By.XPATH,'//a[text()="Click Here to Activate Your Account"]')
        click_link.click()
        # WebDriverWait(driver, 10).until(
        #       EC.element_to_be_clickable((By.XPATH,'//a[text()="Click Here to Activate Your Account"]'))
        #   )

        time.sleep(2)


        driver.get("https://dopamineexchcontrols.wealwindemo.com/login")

        driver.find_element(By.CSS_SELECTOR,"form-control").send_keys("akalal")
       # driver.find_element(By.XPATH,'/html/body/main/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/p[4]/a')

        time.sleep(5)

    # Valid user gamil and invalid password
@pytest.mark.skip
def test_register1(dop):

    how_links = driver.find_elements(By.TAG_NAME,"a")
    print("Number of Links present", len(how_links))

    for link in how_links:
        print(link.text)
    else:print("No links there")

    url = driver.get("https://dopamineexch.wealwindemo.com/https://dopamineexch.wealwindemo.com/")
    print(url)

@allure.severity(allure.severity_level.MINOR)
def test_EmailAlreadyExist(dop):
    driver.get("https://dopamineexch.wealwindemo.com/signup")
    time.sleep(2)

    email_input = driver.find_element(By.NAME,"email")
    email_input.send_keys("dopietesting1@yopmail.com")      # Replace with the email you want to check
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Tester@123")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div[2]/div/div/div/div/form/div[2]/div/span').click()
    driver.execute_script("window.scrollBy(0,400)", "")
    driver.find_element(By.XPATH, '//*[@id="confirmPassword"]').send_keys("Tester@123")
    driver.find_element(By.CSS_SELECTOR, "input#aggree").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#__next > div:nth-child(2) > main > div > div > div.Common_authentication__MicOT > div > div > div > div > form > div.mt-4 > button").click()
    time.sleep(2)

    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "text-red"))
        )

        if "Email already exists" in error_message.text:
            allure.attach(driver.get_screenshot_as_png(), name="AlreadyEmailExist",
                          attachment_type=AttachmentType.PNG)
            print("Email already exists!")
    except TimeoutException:
        print("Email availability unclear")

    # Wait for any indication of the email validation
    """"
    try:
        # Replace "error_message" with the actual ID or class of the element containing the error message
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/div[2]/main/div/div/div[2]/div/div/div/div/form/div[1]/span'))
        )
        # If an error message is found, it means the email already exists
        print("Email already exists")
    except:
        # If no error message is found, the email is likely valid
        print("Email does not exist or is valid")
    #time.sleep(2)
   """

def test_EmailErrorMessage(dop):
    #REGISTER
    driver.get("https://dopamineexch.wealwindemo.com/signup")
    time.sleep(2)

    #Result
   #The 'Invalid email' warning message is displayed.
    try:
        email_input = driver.find_element(By.XPATH, '//input[@name="email"]')
        email_input.send_keys("invalid_email")
        time.sleep(2)

        # FOR INVALID EMAIL
        expected_email_warning_message = "Invalid email"
        assert driver.find_element(By.XPATH,
                                   '//input[@name="email"]/following::span[text()="Invalid email"]').text.__eq__(
            expected_email_warning_message)

        # If the warning message is found, extract its text and compare with the expected value
        actual_warning_message = expected_email_warning_message.text
        expected_email_warning_message = "Invalid email"
        assert actual_warning_message == expected_email_warning_message

    except TimeoutException:
        # If the warning message doesn't appear within the timeout period, handle the timeout exception
        print("Timeout: The 'Invalid email' warning message did not appear within the specified time.")

    except AssertionError:
        # If the actual warning message doesn't match the expected value, handle the assertion error
        print(f"Assertion Error: Expected '{expected_email_warning_message}' but got '{actual_warning_message}'.")

    except Exception as e:
        # Handle any other exceptions that might occur during the process
        print(f"An unexpected error occurred: {e}")

    email_input.text
    password = driver.find_element(By.NAME, "password")
    password.send_keys("Tester@123")
    time.sleep(2)

    driver.execute_script("window.scrollBy(0,400)", "")

    confirm_password = driver.find_element(By.XPATH, '//*[@id="confirmPassword"]')
    confirm_password.send_keys("Tester@123")

    terms_condition = driver.find_element(By.XPATH, '//*[@id="aggree"]')
    terms_condition.click()
    time.sleep(2)

    button_terms_deselect = driver.find_element(By.XPATH, '//*[@id="aggree"]')
    driver.execute_script("arguments[0].checked = false;", button_terms_deselect)
    time.sleep(2)

    is_displayed = driver.execute_script('return arguments[0].offsetParent !== null;',
                                         driver.find_element(By.XPATH, '//span[text()="Invalid email"]'))

    if is_displayed:
        print("The 'Invalid email' warning message is displayed.")
    else:
        print("The 'Invalid email' warning message is not displayed.")

    try:
      submit_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/main/div/div/div[2]/div/div/div/div/form/div[5]/button')
      submit_button.click()
      time.sleep(5)

    except Exception as e:
      # Handle any other exceptions that might occur during the process
      print(f"An unexpected error occurred: {e}")

def test_ErrorMessage(dop):
    # REGISTER
    driver.get("https://dopamineexch.wealwindemo.com/signup")
    time.sleep(2)

    email_input = driver.find_element(By.XPATH, '//input[@name="email"]')     # Result   # The 'Invalid email' warning message is displayed.
    email_input.send_keys("invalid_email")
    time.sleep(2)
    try:

        # FOR INVALID EMAIL
        expected_email_warning_message = "Invalid email"
        assert driver.find_element(By.XPATH,
                                   '//input[@name="email"]/following::span[text()="Invalid email"]').text.__eq__(
            expected_email_warning_message)

        # If the warning message is found, extract its text and compare with the expected value
        actual_warning_message = expected_email_warning_message.text
        expected_email_warning_message = "Invalid email"
        assert actual_warning_message == expected_email_warning_message

    except TimeoutException:
        # If the warning message doesn't appear within the timeout period, handle the timeout exception
        print("Timeout: The 'Invalid email' warning message did not appear within the specified time.")

    except AssertionError:
        # If the actual warning message doesn't match the expected value, handle the assertion error
        print(f"Assertion Error: Expected '{expected_email_warning_message}' but got '{actual_warning_message}'.")

    except Exception as e:
        # Handle any other exceptions that might occur during the process
        print(f"An unexpected error occurred: {e}")

    email_input.text
    password = driver.find_element(By.NAME, "password")
    password.send_keys("Tester@123")
    time.sleep(2)

    driver.execute_script("window.scrollBy(0,400)", "")

    confirm_password = driver.find_element(By.XPATH, '//*[@id="confirmPassword"]')
    confirm_password.send_keys("Tester@123")

    terms_condition = driver.find_element(By.XPATH, '//*[@id="aggree"]')
    terms_condition.click()
    time.sleep(2)

    button_terms_deselect = driver.find_element(By.XPATH, '//*[@id="aggree"]')
    driver.execute_script("arguments[0].checked = false;", button_terms_deselect)
    time.sleep(2)

    is_displayed = driver.execute_script('return arguments[0].offsetParent !== null;',
                                         driver.find_element(By.XPATH, '//span[text()="Invalid email"]'))

    if is_displayed:
        print("The 'Invalid email' warning message is displayed.")
    else:
        print("The 'Invalid email' warning message is not displayed.")

    try:
        submit_button = driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div[2]/main/div/div/div[2]/div/div/div/div/form/div[5]/button')
        submit_button.click()
        time.sleep(5)

    except Exception as e:
        # Handle any other exceptions that might occur during the process
        print(f"An unexpected error occurred: {e}")

    for error in expected_email_warning_message:
        driver.get_screenshot_as_png(error)


