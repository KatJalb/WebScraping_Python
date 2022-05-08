# Webscraping books data from Goodreads
> The main aim of this project is to scrap data on the most upvoted books on the goodreads website. We use three different libraries/frameworks in Python: Beautiful Soup, Scrapy and Selenium and compare their performance.

## Technologies used
- Python - version 3.8.10
- Beautiful Soup
- Scrapy - version 3.0
- Selenium

## Beautiful Soup scrapper
Firstly, we access the main site with a list of books. There we can find links to individual book pages. We scrap those pages using bs.find_all command. We store them in a list and then access them one by one. From each book page, we scrap its title, author, main genre, year, publisher, number of pages, number of ratings and average rating using bs.find command and regular expressions. We store this information in a dictionary and then add it to the dataframe as a new row. 


## Scrapy scrapper
- Opis - 


## Selenium scraper
- Opis -


## Acknowledgements
This project was made as a part of Webscrapping and Social Media Scraping course at Faculty of Economic Sciences, University of Warsaw. 

## Contact
Created by [Kasia](mailto:https://www.katarzyna.jalbrzykowska@student.uw.edu.pl/) and [Monika](mailto:m.kaczan2@student.uw.edu.pl) - feel free to contact us!


