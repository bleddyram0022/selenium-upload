a = () Expected_email = "Email"
    assert driver.find_element(By.XPATH,
                               '//*[@id="__next"]/div[2]/main/div/div/div[2]/div/div/div/div/form/div[1]/label').text.__eq__(Expected_email)

    driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("dopie1@yopmail.com")
