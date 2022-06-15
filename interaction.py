from selenium import webdriver
from selenium.webdriver.common.keys import Keys #to press Enter

chrome_driver_path = "/home/julia/Programs/Chrome-driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_number = driver.find_element_by_id("articlecount")
print(articles_number.text.split()[0])

#articles_number.click() #click on a link

all_portals = driver.find_element_by_link_text("anyone can edit")
#all_portals.click()
search = driver.find_element_by_id("searchInput")
search.send_keys("Python") #type to the search
search.send_keys(Keys.ENTER)

#driver.quit()