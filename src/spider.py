import scrapy
import logging

import scrapy

from src.config import load_config
from scrapy.crawler import CrawlerProcess

logging.getLogger('scrapy').setLevel(logging.WARNING)
logging.getLogger('scrapy').propagate = False

BASE_URL = "https://www.drogaraia.com.br/"

PRODUCTS_SELECTOR = ".products"
URL_SELECTOR = "a::attr(href)"
NEXT_PAGE_SELECTOR = ".next-link a::attr(href)"

class DrogaRaiaSpider(scrapy.Spider):
    def __init__(self):
        self.name = "droga_raia_spider"
        self.config = load_config()
        self.start_urls = self.config["start_urls"]
        self.products=[]

    def parse(self, response):
        print(f"\tSearching product in {response.request.url}")  
        for product in response.css(PRODUCTS_SELECTOR):
            product_url = product.css(URL_SELECTOR).extract_first()
            self.products.append(product_url)
        if "only_first_page" not in self.config or self.config["only_first_page"] is False:
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                next_url = next_page.replace(next_page[0],BASE_URL)
                scrapy.Request(
                    response.urljoin(next_url),
                    callback=self.parse
                )

    def closed(self,reason):
        print(f"{len(self.products)} products found by Droga Raia spider: ")
        url_file_path = self.config["url_file_path"]
        with open(url_file_path,"w") as f:
            print(f"Saving URLs on '{url_file_path}'...")
            for product in self.products:
                f.write(f"{product}\n")  


