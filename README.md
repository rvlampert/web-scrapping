# Web Crawler

* A Web crawler, sometimes called a spider or spiderbot and often shortened to crawler, is an Internet bot that systematically browses the World Wide Web and that is typically operated by search engines for the purpose of Web indexing (web spidering).

* Web search engines and some other websites use Web crawling or spidering software to update their web content or indices of other sites' web content. Web crawlers copy pages for processing by a search engine, which indexes the downloaded pages so that users can search more efficiently.

[Web Crawler - Wikipedia](https://en.wikipedia.org/wiki/Web_crawler)

# Web Scrapping

* Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. Web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser. While web scraping can be done manually by a software user, the term typically refers to automated processes implemented using a bot or web crawler. It is a form of copying in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis.

[Web Scrapping - Wikipedia](https://en.wikipedia.org/wiki/Web_scraping)

# Project

* This project implements a **web crawler**, which is able to identify and index URLs of the products offered by **DrogaRaia's website** and a **Web Scrapper** capable of extracting the **Description**, **Price** and **SKU code** of each of the indexed products.

# URLs

* Base URL:  
```
http://www.drogaraia.com.br/
```
* Start URLs: 
```
https://www.drogaraia.com.br/medicamentos.html
https://www.drogaraia.com.br/beleza.html
https://www.drogaraia.com.br/cabelo.html
https://www.drogaraia.com.br/bem-estar.html
https://www.drogaraia.com.br/mamae-e-bebe.html
```

# Config file

* To facilitate the manual tests and the development of the project, a config.yaml file was created, in which it is possible to configure which are the start urls, the files where the results will be saved, both with the spider and scrapping results, and finally, a variable that indicates if only the first page of each start url should be seen or if the search should be executed in the other pages

* Obs: This last variable regarding the analysis of the first page has the exclusive purpose of making the manual tests easier, since there are thousands of pages and thousands of products, and this could lead to a higher cost of time and resources, so to make it easier to see the correct functioning, it is indicated to set the variable "only_first_page" to True

* Variables:
    - `start_urls`: Contain the URLs used by the spider to search the products URLs
    - `url_file_path`: Contain the path for the spider output
    - `info_file_path`: Contain the path for the scrapping output
    - `only_first_page`: It's a boolean indicating if only the first page of each start url must be used for the spider

# How to run using Docker

To run the complete solution (`web crawler` + `web scrapping`) using Dockerfile, having set the variables in the config file `config.yaml`, just build the docker image by running the `make docker-build` command and run it with the `make docker-run` command

# How to run locally

To run it locally you must first install the dependencies with `make install-dependencies` and run the complete solution (`web crawler` + `web scrapping`) with `make run`.

Locally you can also run each solution separately, to run just the `web crawler` use the `make run-spider` command and to run `web srcapping` use the `make run-scrapping` command

By default the results will be saved in the `results` folder

# How to test

To run the automated tests, run `make test`