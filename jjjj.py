a=open("bala.xls","w")
a.write("no i am  vijay")
a.close()

a = open("bala.xls", "r")
print(a.read())
a.close()

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)