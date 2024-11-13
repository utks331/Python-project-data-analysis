#Scraping Amazon product information using BeautifulSoup
from bs4 import BeautifulSoup
import requests
import csv
import os

# URL and headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
URL = 'https://www.amazon.in/Sony-CFI-2008A01X-PlayStation%C2%AE5-Console-slim/dp/B0CY5HVDS2/ref=sr_1_3?crid=25M9MB9VETNLY&dib=eyJ2IjoiMSJ9.pFhgCqcURNHp7Ghh6tpkbk5t9SODgbdrDwEIjCKk_gJJywLWhKolbOXvQNDoYMM4xcMG07Vc_KuhTgDS-2bxzXvxI9Y9TyBJ_mTsB090A3laSTfc2X6B_wuAWZcQuDzZWBCESHvGi-N58Aht30_c7TbXJd-45qln8RXFiUBLAPUibDo8d1qmmBXYuJjgp0UApIL3Co3cfRWa4smfB0xKKMdJwd9sup0mFRycRMVqNeo.ccUxOB42_q27zxOml8GJ4W57qqDNbueBIrM0aHwfevk&dib_tag=se&keywords=playstation+5&qid=1731046591&sprefix=playstation+5+%2Caps%2C224&sr=8-3'



# Sending request and creating soup object
webpage = requests.get(URL, headers=HEADERS)
print("Status Code:", webpage.status_code)

# Check if page content was retrieved
if webpage.status_code == 200:
    soup = BeautifulSoup(webpage.content, "lxml")

    # Print the entire HTML for debugging (optional)
    # print(soup.prettify())

    # Retrieving product title
    try:
        title = soup.find("span", attrs={"id": "productTitle"})
        title_string = title.get_text(strip=True).replace(',', '') if title else "NA"  # Removes commas
        print('Product Title =', title_string)
    except AttributeError:
        title_string = "NA"
        print('Product Title not found')

    price_string = "NA"
    try:
        price = (soup.find("span",attrs={"class":"a-price-whole"}) or
        soup.find("span", class_="price") or 
        soup.find("span", id="priceblock_ourprice") or 
        soup.find("span", id="priceblock_dealprice"))
        if price:
            price_string = price.get_text(strip=True).replace(',','')
        else:
            price_string = 'NA'
        print('Product_price==',price_string)
    except AttributeError:
        price_string = 'NA'
        print('Product price not found')
    


    file_exists = os.path.isfile('out.csv') #Check if the file already exists
    # Saving current information in a CSV file
    with open('out.csv', 'a',newline='') as File:
        writer = csv.writer(File)
        if not file_exists:
            writer.writerow(["Product_title","Product_price"])
        writer.writerow([title_string,price_string])
else:
    print("Failed to retrieve the page content.")

