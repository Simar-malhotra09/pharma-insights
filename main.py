from scraper.pharma.bio_pharma_dive import BioPharmaDiveScraper
from scraper.scraper import Scraper
import json

def main():
    scraper = Scraper()  
    config = scraper.config  
    companies = scraper.companies  

    
    bio_pharma_dive_scraper = BioPharmaDiveScraper(config, companies)
    all_articles = bio_pharma_dive_scraper.scrape_website(config, companies)

    # Save the filtered articles to a JSON file
    with open('data/filtered_articles.json', 'w') as outfile:
        json.dump(all_articles, outfile, indent=4)

if __name__ == "__main__":
    main()
