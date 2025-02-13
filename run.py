from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions();
driver = webdriver.Chrome(options = chrome_options)
sleep(1)

driver.get('https://www.pinterest.com/')  
sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/button/div/div").click()
sleep(2)

driver.find_element(By.ID, "email").send_keys("hejunguyen@gmail.com")
sleep(2)

driver.find_element(By.ID, "password").send_keys("trunghieu")
sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[1]/form/div[7]/button/div").click()
sleep(2)