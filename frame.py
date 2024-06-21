import unittest

import frame
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class TestErrorMessage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Initialize your WebDriver
        self.driver.maximize_window()  # Maximize the browser window
        self.driver.implicitly_wait(10)  # Implicitly wait for elements to be found

    def test_error_message(self):
        driver = self.driver

        driver.get("https://dopamineexch.wealwindemo.com/signup")
        time.sleep(2)

        email_input = driver.find_element(By.XPATH, '//input[@name="email"]')
        email_input.send_keys("invalid_email")
        time.sleep(2)

        password = driver.find_element(By.NAME, "password")
        password.send_keys("Tester@123")
        time.sleep(2)

        error_message_xpath = '//*[@id="__next"]/div[2]/main/div/div/div[2]/div/div/div/div/form/div[1]/span'
        expected_error_message = "Invalid email"
        try:
            error_message_element = driver.find_element(By.XPATH, error_message_xpath)
            error_message_text = error_message_element.text
            self.assertEqual(error_message_text, expected_error_message,
                             f"Expected: {expected_error_message}, Actual: {error_message_text}")
        except NoSuchElementException:
            self.fail("Error message element not found")

    def tearDown(self):
        self.driver.quit()  # Close the browser window


if __name__ == "__main__":
    unittest.main()
