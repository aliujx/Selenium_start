from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/julia/Programs/Chrome-driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element_by_name("fName")
first_name.send_keys("Julia")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Diadkova")

email = driver.find_element_by_name("email")
email.send_keys("julia@mail.com")

sign_up = driver.find_element_by_class_name("btn")
sign_up.click()
