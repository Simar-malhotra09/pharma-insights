import requests
import json
import time
import random
from bs4 import BeautifulSoup
class Scraper:
    def __init__(self, config=None, companies=None, config_file='/Users/simarmalhotra/Desktop/projects/pharma/sites_config.json', companies_file='/Users/simarmalhotra/Desktop/projects/pharma/data/pharma.json'):

        if config is None:
            self.config = self.load_config(config_file)
        else:
            self.config = config
        
        if companies is None:
            self.companies = self.load_companies(companies_file)
        else:
            self.companies = companies

    def load_config(self, file_path):
        """Load website configurations from a file."""
        with open(file_path, 'r') as file:
            return json.load(file)

    def load_companies(self, file_path):
        """Load the list of companies to filter articles."""
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'companies' in data:
                return set(data['companies'])
            else:
                raise ValueError("The key 'companies' is missing in the input JSON.")
            


    def scrape_website(self, config, companies):
        """Scrape articles from a given website based on the config."""
        raise NotImplementedError("scrape_website method must be overridden by subclass.")




