from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
name = input("instagram username : ") 
password = input("instagram password : ")
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()
driver.implicitly_wait(10) 
driver.find_element_by_name("username").send_keys(name)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF").click()
time.sleep(10)
driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF").click()