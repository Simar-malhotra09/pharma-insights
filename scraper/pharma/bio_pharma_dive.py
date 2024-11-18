import requests
from bs4 import BeautifulSoup
from scraper.scraper import Scraper

class BioPharmaDiveScraper(Scraper):  


    def scrape_website(self, config, companies):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.1 Safari/537.36'
        }

        response = requests.get(config['biopharmadive']['base_url'], headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Select the articles based on the site's configuration
        articles = soup.select(config['biopharmadive']['article_selector'])
        filtered_articles = []
        count = 0

        for article in articles:
            if count >= 3:  # Limit to 3 articles
                break

            title = article.get_text(strip=True)
            link_tag = article.find(config['biopharmadive']['link_selector'])
            if not link_tag or not link_tag.get('href'):
                continue

            link = link_tag['href']
            if not link.startswith("http"):
                link = config['biopharmadive']['link_prefix'] + link

            date_tag = article.find_next("span", class_="date d-inline-block")
            date = date_tag.get_text(strip=True) if date_tag else "N/A"

            if any(company.lower() in title.lower() for company in companies):
                count += 1
                filtered_articles.append({
                    "title": title,
                    "link": link,
                    "date": date
                })

        return filtered_articles
