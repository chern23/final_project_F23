# SELENIUM 2 - this code prints to a JSON file

import time
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() 

url = "https://www.clevelandart.org/art/collection/search?i=1&search=flower"
driver.get(url)

# Simulate scrolling down to trigger more content loading
scroll_limit = 52  

for _ in range(scroll_limit):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(1.5)  

    # Wait for new content to be loaded
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'search-result'))
    )

page_source = driver.page_source

driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

results = []
artworks = soup.find_all("div", {"class": "search-result grid-item"})

for artwork in artworks:

    artwork_url = "https://www.clevelandart.org" + artwork.find("a")["href"]
    artwork_soup = BeautifulSoup(requests.get(artwork_url).content, "html.parser")

    title_element = artwork_soup.find('h1', class_='field field-name-field-primary-title field-type-text field-label-hidden')
    title = title_element.text.strip() if title_element else None

    date_element = artwork_soup.find('p', class_='field field-name-field-date-text field-type-text field-label-hidden') 
    date = date_element.text.strip() if date_element else None

    country_element = artwork_soup.find('p', class_='field field_name_field_creation_text')
    country = country_element.text.strip() if country_element else None

    description_element = artwork_soup.find('div', class_='field field-name-field-description field-type-text-long field-label-above')
    description = description_element.text.strip() if description_element else None

    class_element = artwork_soup.find('div', class_='field field-name-field-classification-text')
    classification = class_element.text.strip() if class_element else None

    result = {
            'Title': title,
            'Period': date,
            'Country': country,
            'Description': description,            
            'Classification': classification
        }
    
    results.append(result)

json_file_path = 'cleveland_flower_artworks.json'

# ensure_ascii=FALSE fixed unicode errors!
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(results,json_file, indent=2, ensure_ascii=False)

print(f"Results written to {json_file_path}")








#------------------ CODE NOT USED -------------------

# SELENIUM 1 - this code prints to a csv file

# import time
# import csv
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()  

# url = "https://www.clevelandart.org/art/collection/search?i=1&search=flower"
# driver.get(url)

# # Simulate scrolling down to trigger more content loading
# scroll_limit = 53  

# for _ in range(scroll_limit):
#     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
#     time.sleep(1.5)  

#     # Wait for new content to be loaded
#     WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'search-result'))
#     )

# page_source = driver.page_source

# driver.quit()

# soup = BeautifulSoup(page_source, 'html.parser')

# results = []
# artworks = soup.find_all("div", {"class": "search-result grid-item"})

# for artwork in artworks:

#     artwork_url = "https://www.clevelandart.org" + artwork.find("a")["href"]
#     artwork_soup = BeautifulSoup(requests.get(artwork_url).content, "html.parser")

#     title_element = artwork_soup.find('h1', class_='field field-name-field-primary-title field-type-text field-label-hidden')
#     title = title_element.text.strip() if title_element else None

#     date_element = artwork_soup.find('p', class_='field field-name-field-date-text field-type-text field-label-hidden') 
#     date = date_element.text.strip() if date_element else None

#     country_element = artwork_soup.find('p', class_='field field_name_field_creation_text')
#     country = country_element.text.strip() if country_element else None

#     description_element = artwork_soup.find('div', class_='field field-name-field-description field-type-text-long field-label-above')
#     description = description_element.text.strip() if description_element else None

#     class_element = artwork_soup.find('div', class_='field field-name-field-classification-text')
#     classification = class_element.text.strip() if class_element else None

#     results.append({'Title': title, 'Period': date,'Country': country, 'Description': description, 'Classification': classification})

# csv_file_path = 'cleveland_flower_artworks.csv'
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Title', 'Period', 'Country', 'Description', 'Classification']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()

#     writer.writerows(results)

# print(f"Results written to {csv_file_path}")
