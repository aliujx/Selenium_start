from selenium import webdriver
import pandas as pd

chrome_driver_path = "/home/julia/Programs/Chrome-driver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
#driver.get('https://www.amazon.com/DJI-Smartphone-Stabilizer-Extension-ShotGuides/dp/B099ZXD27F/ref=sr_1_26?qid=1654962791&s=electronics&sr=1-26') #open a page
#price = driver.find_element_by_id('priceblock-outprice')
#driver.find_element_by_name('q')
#print(price.text)

#driver.close() #close a page
#driver.quit() #close whole browser

driver.get("https://www.python.org/")
#search_bar = driver.find_element_by_name('q')
#print(search_bar.get_attribute('placeholder'))

#logo = driver.find_element_by_class_name('python-logo')
#print(logo.size)

#documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
#print(documentation_link)

#bug_link = driver.find_element_by_xpath('https://docs.python.org/3/tutorial/controlflow.html#defining-functions')
#print(bug_link.text)

event_times = driver.find_elements_by_css_selector('.last time')
event_names = driver.find_elements_by_css_selector('.last li a')
#for time in event_times:
    #print(time.text)
events = {}
for n in range(len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[n].text
    }
print(events)

driver.quit()