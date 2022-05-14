from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
import pandas as pd
import re
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# Performance measurement - start:
t0 = time.time()

# Defining parameters limiting the number of pages to scrap:
limit = True
pages = 3

# Init:
gecko_path = '/usr/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = True
driver = webdriver.Firefox(options = options, service=ser)

# Finding the links to all sites we want to scrap
# Each page name is build as url+'i' where i is limited with the parameter 'pages'
url = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page='
books_links=[]
for i in range(1,pages+1):
    driver.get(url+str(i))
    time.sleep(0.5)

    # each book's link is found by XPATH: by tag and attribute 'class'
    # the list of links is created with the attributes 'href'
    books = driver.find_elements(By.XPATH, '//a[@class="bookTitle"]')
    books_links_i = [x.get_attribute('href') for x in books]
    books_links = books_links + books_links_i

# Creating dataframe for the data
d = pd.DataFrame({'title': [], 'author': [], 'year': [], 'publisher': [], 'genre': [], 'pages': [], 'no. of ratings': [], 'rating': []})

# Limiting the number of links (books) to scrap
if limit:
    books_list = books_links[0:100]
else:
    books_list = books_links

# Scrapping the data from each book page
for i,link in enumerate(books_list):

    # Now we focus on idividual links to book pages
    driver.get(link)
    time.sleep(0.5)
    
    # For the first link we need to dismiss the 'login' pop-up
    try:
        if i==0:
            # Finding the 'dismiss' button
            dis=driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/button')
            dis.click()
    except:
        pass

    # Finding the data by XPATH
    title = driver.find_element(By.XPATH, '//h1[@id="bookTitle"]').text.strip()
    time.sleep(0.1)
    author = driver.find_element(By.XPATH, '//span[@itemprop="name"]').text.strip()
    time.sleep(0.1)
    year = driver.find_element(By.XPATH, '(//div[@id="details"]/div[@class="row"])[2]').text.strip()
    try:
        year = re.findall('[0-9]{4}', year)[0]
    except:
        year = ''
    time.sleep(0.1)
    publisher = driver.find_element(By.XPATH, '(//div[@id="details"]/div[@class="row"])[2]').text.strip()
    try:
        publisher = re.findall('by.+', publisher)[0][3:].strip()
    except:
        publisher = ''
    try:
        child = driver.find_element(By.XPATH, '(//div[@id="details"]/div[@class="row"])[2]/nobr').text
        publisher = publisher.replace(child, '').strip()
    except:
        pass
    time.sleep(0.1)
    genre = driver.find_element(By.XPATH, '//a[@class="actionLinkLite bookPageGenreLink"]').text.strip()
    time.sleep(0.1)
    pages = driver.find_element(By.XPATH, '//span[@itemprop="numberOfPages"]').text.strip()
    try:
        pages = re.findall('[0-9]+', pages)[0]
    except:
        pages = ''
    time.sleep(0.1)
    no_ratings = driver.find_element(By.XPATH, '//meta[@itemprop="ratingCount"]').get_attribute('content')
    time.sleep(0.1)
    rating = driver.find_element(By.XPATH, '//span[@itemprop="ratingValue"]').text.strip()
    time.sleep(0.1)
    
    # Creating a dictionay with the scrapped data:
    book = {'title': title, 'author': author, 'year': year, 'publisher': publisher, 'genre': genre, 'pages': pages, 'no. of ratings': no_ratings, 'rating': rating}
    
    # Adding our data to the dataframe
    d = d.append(book, ignore_index = True)
    time.sleep(0.1)

# Close browser:
driver.quit()

print(d)
# Saving scrapped data to the *.csv file
d.to_csv('books_Sel.csv')

# Performance measurement - end:
t1 = time.time()
total_time = t1-t0
print(total_time)
