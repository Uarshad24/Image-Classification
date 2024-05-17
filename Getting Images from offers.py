from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import os
import numpy as np


data_array = np.genfromtxt('Alsvinlist.csv', delimiter=',', dtype=str)
add_list = data_array.tolist()
a=1
i=1
for url in add_list:
    if a < 1:
        a= a+1
        continue;
    else:
        driver = webdriver.Firefox()
        driver.get(url)

        source_data = driver.page_source
        soup = bs(source_data,features="html.parser")

        imgs = soup.find_all('img')
        image_urls = [img.get('src') for img in imgs if 'ad_pictures' in img.get('src')]
        print("ad#",a, "photos available=" , len(image_urls))
 
        folder_path = r'C:\Users\Muhammad Mursaleen\.spyder-py3\Alsvin'


        for imageurl in image_urls:
            response = requests.get(imageurl)
            with open(os.path.join(folder_path, f"picture{i}.jpg"), 'wb') as file:
                file.write(response.content)
                i=i+1   
                print("Image downloaded successfully")
            
        driver.quit()
        a= a+1        