# sym svelte-eurwtr
import requests
import json
from bs4 import BeautifulSoup


# def scrape_website():

#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.1 Safari/537.36'
#         }
        

#         response = requests.get('https://stockanalysis.com/stocks/industry/biotechnology/', headers=headers)
#         if response.status_code != 200:
#             print(f"Failed to retrieve the page. Status code: {response.status_code}")
#             return 
    

#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Select the articles based on the site's configuration
#         table = soup.find("table", id="main-table")
#         if not table:
#             print("Table not found")
#             return

#         # Extract rows from the table
#         rows = table.find_all("tr")
#         stocks=[]
        
#         column_index = 1
#         for row in rows:
#             cells = row.find_all("td")
#             if len(cells) > column_index:
#                 print(cells[column_index].get_text(strip=True))
#                 stocks.append(cells[column_index].get_text(strip=True))

        
#         with open('data/biotech.json', 'w') as f:
#             json.dump(stocks, f, indent=4)

#         return stocks

# s= scrape_website()


import yfinance as yf

with open('data/biotech.json', 'r') as f:
    data = json.load(f)


d = {}

for ticker in data:
    stock = yf.Ticker(ticker)
    
    company_info = stock.info
    company_name = company_info.get('longName', 'Unknown Company')
    
    print(f"Ticker: {ticker}, Company: {company_name}")
    
    # Store in dictionary
    d[ticker] = company_name


with open('data/biotech.json', 'w') as f:
    json.dump(d, f, indent=4)

print("Updated data saved to biotech.json.")


