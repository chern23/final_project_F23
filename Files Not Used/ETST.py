# TEST NEW
import requests
from bs4 import BeautifulSoup
import csv
import time

def get_wikidata_info(qid):
    # Define the Wikidata API endpoint
    wikidata_api_url = f"https://www.wikidata.org/w/api.php"

    # Specify parameters for the API request
    params = {
        'action': 'wbgetentities',
        'ids': qid,
        'format': 'json'
    }

    # Make the API request
    response = requests.get(wikidata_api_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(response.content)

get_wikidata_info("Q20173083")





# results = []
# i = 0 


# url = f"https://www.nga.gov/collection-search-result.html?title=flower&pageSize=30&pageNumber={i}"
# scraper = cloudscraper.create_scraper(interpreter='nodejs')
# content = scraper.get(url).content
# national_soup = BeautifulSoup(content, "html.parser")

# print(national_soup.prettify())

# artworks = national_soup.find_all("dt", {"class": "title"})
# print("Artworks found", len(artworks))

# while i <= 2: 
#     for artwork in artworks:
#         time.sleep(0.5)
#         artwork_url = "https://www.nga.gov" + artwork.find("a")["href"]
#         artwork_soup = BeautifulSoup(scraper.get(artwork_url).content, "html.parser")

#         accessionNo = artwork_soup.find_all('p', class_='object-attr-value').text.strip()        
#         country = artwork_soup.find_all('span', class_='object-artist').text.strip()


        # accession_element = artwork.find('p', class_='object-attr-value')
        # accessionNo = accession_element.text.strip() if accession_element else None

        # country_element = artwork.find('span', class_='object-artist')
        # country = country_element.text.strip() if country_element else None

        # results.append({'Accession Number': accessionNo, 'Country of Creation': country})
        
#         results.append({'Accession Number': accessionNo, 'Country': country})

#     i += 1

# # Move CSV writing outside the loop
# csv_file_path = 'test_expanded.csv'
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Accession Number', 'Creation']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()

#     writer.writerows(results)

# print(f"Results written to {csv_file_path}")







# import requests
# from bs4 import BeautifulSoup
# import csv

# base_url = "https://www.nga.gov/collection-search-result.html"
# search_term = "flower"
# page_size = 30

# results = []

# def scrape_page(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         # Extract information from the current page, modify as needed
#         # Example: title_elements = soup.find_all('h3', class_='title-class')
#         # Extract other relevant information and append to the results list
#         # Example: for title_element in title_elements:
#         #              title = title_element.text.strip()
#         #              results.append({'Title': title})
#     else:
#         print(f"Error accessing page {url}. Status code: {response.status_code}")

# # Determine the total number of pages
# # In this example, we'll assume you know the total number of pages or need to determine it programmatically
# total_pages = 10  # You may adjust this based on your actual knowledge or by inspecting the website

# # Loop through the pages
# for page_number in range(1, total_pages + 1):
#     url = f"{base_url}?title={search_term}&pageSize={page_size}&pageNumber={page_number}"
#     scrape_page(url)

# # Writing results to a CSV file
# csv_file_path = 'nga_results.csv'
# fieldnames = ['Title']  # Adjust these based on the actual data you're extracting

# with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     # Write header
#     writer.writeheader()

#     # Write rows
#     writer.writerows(results)

# print(f"Results written to {csv_file_path}")







# # TEST2
# import requests
# from bs4 import BeautifulSoup
# import csv
# import time

# url = "https://www.clevelandart.org/art/collection/search?i=1&search=flower"
# cleveland_soup = BeautifulSoup(requests.get(url).content, "html.parser")

# results = []
# i = 0 #image

# while i <= 2: 
#     #to slow down cloudscraper
#     time.sleep(1)
#     url = f"https://www.nga.gov/collection-search-result.html?title=flower&pageSize=30&pageNumber={i}" 
#     i+=1 #adding increment


#     artworks = cleveland_soup.find_all("div", {"class" : "section-col banner-right"})

#     for artwork in artworks:

#         artwork_url = "https://www.nga.gov" + artwork.find("a")["href"]
#         artwork_soup = BeautifulSoup(requests.get(artwork_url).content, "html.parser")

#         accession_element = artwork.find('div', class_='object-attr accession')
#         accessionNo = accession_element.text.strip() if accession_element else None

#         country_element = artwork.find('div', class_='object-attr accession')
#         country = country_element.text.strip() if country_element else None

#         results.append({'Accession Number': accessionNo, 'Country of Creation': country})

#     # Move CSV writing outside the loop
#     csv_file_path = 'national_additional.csv'
#     with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['Accession Number', 'Country of Creation']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()

#         writer.writerows(results)

#     print(f"Results written to {csv_file_path}")





# #NEW ATTEMPT

# import requests
# from bs4 import BeautifulSoup
# import csv
# import time

# # url = "https://www.clevelandart.org/art/collection/search?i=1&search=flower"

# results = []
# i = 0 

# while True:
# # while i <= 2:
#     time.sleep(1)
    
#     url = f"https://www.nga.gov/collection-search-result.html?title=flower&pageSize=30&pageNumber={i}"
#     national_soup = BeautifulSoup(requests.get(url).content, "html.parser")

#     artworks = national_soup.find_all("li", {"class": "art"})

#     for artwork in artworks:
#         artwork_url = "https://www.nga.gov" + artwork.find("a")["href"]
#         artwork_soup = BeautifulSoup(requests.get(artwork_url).content, "html.parser")

#         accession_element = artwork.find('p', class_='object-attr-value')
#         accessionNo = accession_element.text.strip() if accession_element else None

#         country_element = artwork.find('span', class_='object-artist')
#         country = country_element.text.strip() if country_element else None

#         results.append({'Accession Number': accessionNo, 'Country of Creation': country})

#     # Break the loop if there are no more results
#     if not artworks:
#         break

# # Move CSV writing outside both loops
# csv_file_path = 'national_additional.csv'
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile: 
#     fieldnames = ['Accession Number', 'Country of Creation']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerows(results)

# i += 1  # Increment page number

# print(f"Results written to {csv_file_path}")





# #NEW ATTEMPT 2

# import requests
# from bs4 import BeautifulSoup
# import json
# import time

# results = []
# i = 0  

# while i <= 1:
#     time.sleep(1)
#     url = f"https://www.nga.gov/collection-search-result.html?title=flower&pageSize=30&pageNumber={i}"
#     national_soup = BeautifulSoup(requests.get(url).content, "html.parser")

#     artworks = national_soup.find_all("li", {"class": "art"})
    
#     for artwork in artworks:
#         artwork_url = "https://www.nga.gov" + artwork.find("a")["href"]
#         artwork_soup = BeautifulSoup(requests.get(artwork_url).content, "html.parser")

#         accession_element = artwork.find('div', class_='object-attr accession')
#         accessionNo = accession_element.text.strip() if accession_element else None

#         country_element = artwork.find('span', class_='object-artist')
#         country = country_element.text.strip() if country_element else None

#         results.append({'Accession Number': accessionNo, 'Country of Creation': country})

#     # # Break the loop if there are no more results
#     # if not artworks:
#     #     break

#         i += 1  # Increment page number

#         # Writing results to a JSON file
#     json_file_path = 'national.json'

#     with open(json_file_path, 'w', encoding='utf-8') as json_file:
#         json.dump(results,json_file, indent=2)

#     print(f"Results written to {json_file_path}")

# # # Move CSV writing outside both loops
# # csv_file_path = 'national_additional.csv'
# # with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
# #     # fieldnames = ['Accession Number', 'Country of Creation']
# #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

# #     writer.writeheader()
# #     writer.writerows(results)

# # print(f"Results written to {csv_file_path}")






# # NEW ATTEMPT 3
# import requests
# from bs4 import BeautifulSoup
# import csv
# import time

# def get_artwork_urls(base_url, page_number):
#     url = f"{base_url}&pageSize=30&pageNumber={page_number}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         artwork_links = soup.select('.search-result__image a')
#         return [link['href'] for link in artwork_links]
#     else:
#         print(f"Error accessing page {url}. Status code: {response.status_code}")
#         return []

# def scrape_artwork_page(artwork_url):
#     response = requests.get(artwork_url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         accession_element = soup.find('p', class_='object-attr-value')
#         accession_number = accession_element.text.strip() if accession_element else None

#         artist_element = soup.find('span', class_='object-artist')
#         artist = artist_element.text.strip() if artist_element else None

#         return {'Accession Number': accession_number, 'Artist/Maker': artist}
#     else:
#         print(f"Error accessing page {artwork_url}. Status code: {response.status_code}")
#         return {}

# # Main scraping process
# base_search_url = "https://www.nga.gov/collection-search-result.html?title=flower"
# results = []

# # Iterate over pages
# for page_number in range(1, 3):  # Adjust the range as needed
#     artwork_urls = get_artwork_urls(base_search_url, page_number)
    
#     # Iterate over individual artwork pages
#     for artwork_url in artwork_urls:
#         time.sleep(1)  # To avoid making too many requests in a short time
#         artwork_data = scrape_artwork_page(artwork_url)
#         results.append(artwork_data)

# # Write results to a CSV file
# csv_file_path = 'nga_results.csv'
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Accession Number', 'Artist/Maker']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(results)

# print(f"Results written to {csv_file_path}")




# # ONLINE HELP

# import requests
# from bs4 import BeautifulSoup
# import csv
# import time

# # results = []


# url = "https://www.nga.gov/collection-search-result.html?title=flower&pageSize=30&pageNumber=1"
# national_soup = BeautifulSoup(requests.get(url).content, "html.parser")

# artworks = national_soup.find_all('li', class_='art')

# for artwork in artworks:
#     print(artwork.find('h1'))
#     # print(artwork.find('span', class_='category'))

# #     for artwork in artworks:
# #         artwork_url = "https://www.nga.gov" + artwork.find("a")["href"]
# #         artwork_soup = BeautifulSoup(requests.get(artwork_url).content, "html.parser")

# #         accession_element = artwork.find('p', class_='object-attr-value')
# #         accessionNo = accession_element.text.strip() if accession_element else None

# #         country_element = artwork.find('span', class_='object-artist')
# #         country = country_element.text.strip() if country_element else None

# #         results.append({'Accession Number': accessionNo, 'Country of Creation': country})
