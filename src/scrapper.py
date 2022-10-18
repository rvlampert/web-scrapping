import scrapy
import logging
from pprint import pprint
import scrapy
import ast

from scrapy.crawler import CrawlerProcess
from src.config import load_config

logging.getLogger('scrapy').setLevel(logging.WARNING)
logging.getLogger('scrapy').propagate = False

INFO_SELECTOR = "head > script"

class DrogaRaiaScrapper(scrapy.Spider):

    def __init__(self):
        self.name = "droga_raia_scrapper"
        self.config = load_config()
        self.start_urls = get_products_urls(self.config)
        self.products=[]

    def parse(self, response):
        print(f"\tAnalysing product of {response.request.url}")
        info = response.css(INFO_SELECTOR).extract_first()
        info = string_to_dict(info)
        product_info = f"Nome=\"{info.get('name')}\" Preco=R${info.get('offers').get('price')} SKU={info.get('sku')}"
        self.products.append(product_info)

    def closed(self,reason):
        info_file_path = self.config["info_file_path"]
        with open(info_file_path,"w") as f:
            print(f"Saving informations on '{info_file_path}'...")
            for product in self.products:
                f.write(f"{product}\n")

def get_products_urls(config):
    url_file_path = config["url_file_path"]
    with open(url_file_path, "r") as f:
        return f.readlines() 

def string_to_dict(info):
    info = info.replace('<script type="application/ld+json">',"")
    info = info.replace('</script>',"")
    return ast.literal_eval(info)
