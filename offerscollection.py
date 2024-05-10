from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from time import sleep
import csv
url_main_page = "https://www.pakwheels.com/"
Car = 'Alsvin'

driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url_main_page)
sleep(10)

search_input = driver.find_element(By.CSS_SELECTOR, "input#home-query.ui-autocomplete-input")
search_input.send_keys(Car)
submit_button = driver.find_element(By.XPATH, "//*[@id='home-search-btn']")
submit_button.click()
sleep(5)

ads = []
i = 1
while i < 25:
    sleep(2)
    source_data = driver.page_source
    soup = bs(source_data,features="html.parser")
    elements = driver.find_elements(By.CSS_SELECTOR, "div[class*='ad-container'] a")
    
    for element in elements:
        href = element.get_attribute("href")
        ads.append(href)  
    i = i + 1
    sleep(2)
    try:
        cross = f"https://www.pakwheels.com/used-cars/search/-/?q={Car}&page={i}"            
        driver.get(cross)
    except:
        break;

lists = [[item] for item in ads]
with open('Alsvinlist.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(lists)