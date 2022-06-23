import os
from selenium import webdriver
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

driver.get("https://www.neoapgh.com/#/login")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@placeholder='Please enter your mobile number']").send_keys("278179745")
driver.find_element(By.XPATH, "//input[@placeholder='Please enter the password']").send_keys("123abcT")
driver.find_element(By.CLASS_NAME, "login-btn").click()




driver.switch_to.new_window('tab')
driver.get("https://www.neoapgh.com/#/startMining")

driver.find_element(By.XPATH, "//button[@class='btn-b van-button van-button--info van-button--normal van-button--round']").click()


