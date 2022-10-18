import sys

import scrapy
from scrapy.crawler import CrawlerProcess

from multiprocessing.context import Process
from src.spider import DrogaRaiaSpider
from src.scrapper import DrogaRaiaScrapper

def run(Crawler):
    crawler = CrawlerProcess()
    crawler.crawl(Crawler)
    crawler.start()

def main():
    args = sys.argv[1:]
    process_spider = Process(target=run, kwargs={"Crawler":DrogaRaiaSpider})
    process_scrapper = Process(target=run, kwargs={"Crawler":DrogaRaiaScrapper})
        
    if len(args) == 1:
        if args[0] == 'spider':
            print("Running spider")
            process_spider.start()
            process_spider.join()
        elif args[0] == 'scrapper':
            print("Running scrapper")
            process_scrapper.start()
            process_scrapper.join()
        
    elif len(args) == 0:
        print("Running spider and scrapper")
        process_spider.start()
        process_spider.join()
        process_scrapper.start()
        process_scrapper.join()

    else:
        print("Numero de argumentos invalidos")
    
if __name__ == '__main__':
    main()



    