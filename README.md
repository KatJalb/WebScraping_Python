# Webscraping books data from Goodreads
> The main aim of this project is to scrap data on the most upvoted books on the goodreads website. We use three different libraries/frameworks in Python: Beautiful Soup, Scrapy and Selenium and compare their performance.

## Technologies used
- Python - version 3.8.10
- Beautiful Soup
- Scrapy - version 3.0
- Selenium

## Description of our scraper mechanics

Firstly, we access the main site with a list of books. There we can find links to individual book pages. The complete list is divided into 100 pages, which contains 100 books. Therefore, we dedided to limit our scrapping to the first ... pages. The variable 'pages' is defined at the begining of each code. We store the links in a list and then access them one by one. From each book page, we scrap its title, author, main genre, year, publisher, number of pages, number of ratings and average rating using commands and regular expressions. We store this information in a dictionary and then add it to the dataframe as a new row or export the results to the external *.csv file (scrapy). 


## Methods used for scrapping

Beautiful Soup scrapper
- bs.find_all
- bs.find
- re.findall

Scrapy scrapper
- scrapy.Field
- response.xpath().getall()
- response.xpath().re()

Selenium scraper
- webdriver.Firefox
- driver.find_elements(By.XPATH,)
- re.findall

## Setup

To run this project from command-line, go to the correct directory and use following commands:

Beautiful Soup:
 'soup' directory
```
$ python3 *.py
```

Scrapy:
 'project_scrapy' top level directory
 - First step (creating link_lists.csv):
```
$ scrapy crawl link_lists -o link_lists.csv
```
 - Second step (creating books.csv )
```
$ scrapy crawl books -o books.csv
```

Selenium:
 'selenium' directory
```
$ python3 Sel.py
```


## Acknowledgements
This project was made as a part of Webscrapping and Social Media Scraping course at Faculty of Economic Sciences, University of Warsaw. 

## Contact
Created by [Kasia](mailto:https://www.katarzyna.jalbrzykowska@student.uw.edu.pl/) and [Monika](mailto:m.kaczan2@student.uw.edu.pl) - feel free to contact us!


