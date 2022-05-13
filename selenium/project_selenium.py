from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
import datetime
import pandas as pd
import re

t0 = time.time()

# Init:
gecko_path = '/usr/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = True
driver = webdriver.Firefox(options = options, service=ser)

url = 'https://www.goodreads.com/list/show/1'

# Actual program:
driver.get(url)
time.sleep(3)

# Finding the links to all sites we want to scrap
books = driver.find_elements(By.XPATH, '//a[@class="bookTitle"]')
books_links = [x.get_attribute('href') for x in books]



# Creating dataframe for the data
d = pd.DataFrame({'title': [], 'author': [], 'year': [], 'publisher': [], 'genre': [], 'pages': [], 'no. of ratings': [], 'rating': []})

for link in books_links[0:5]:

    # Now we focus on idividual links to book pages
    driver.get(link)
    time.sleep(3)
    
    #dis=driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/button')
    #dis.click()
    #time.sleep(5)

    title = driver.find_element(By.XPATH, '//h1[@id="bookTitle"]').text.strip()
    time.sleep(0.1)
    author = driver.find_element(By.XPATH, '//span[@itemprop="name"]').text.strip()
    time.sleep(0.1)
    year = driver.find_element(By.XPATH, '(//div[@id="details"]/div[@class="row"])[2]').text.strip()
    year = re.findall('[0-9]{4}', year)[0]
    time.sleep(0.1)
    publisher = driver.find_element(By.XPATH, '(//div[@id="details"]/div[@class="row"])[2]').text.strip()
    publisher = re.findall('by.+', publisher)[0][3:].strip()
    try:
        child = driver.find_element(By.XPATH, '(//div[@id="details"]/div[@class="row"])[2]/nobr').text
        publisher = publisher.replace(child, '').strip()
    except:
        pass
    
    time.sleep(0.1)
    genre = driver.find_element(By.XPATH, '//a[@class="actionLinkLite bookPageGenreLink"]').text.strip()
    time.sleep(0.1)
    pages = driver.find_element(By.XPATH, '//span[@itemprop="numberOfPages"]').text.strip()
    pages = re.findall('[0-9]+', pages)[0]
    time.sleep(0.1)
    no_ratings = driver.find_element(By.XPATH, '//meta[@itemprop="ratingCount"]').get_attribute('content')
    time.sleep(0.1)
    rating = driver.find_element(By.XPATH, '//span[@itemprop="ratingValue"]').text.strip()
    time.sleep(0.1)

    book = {'title': title, 'author': author, 'year': year, 'publisher': publisher, 'genre': genre, 'pages': pages, 'no. of ratings': no_ratings, 'rating': rating}
    
    d = d.append(book, ignore_index = True)
    time.sleep(0.1)

# Close browser:
driver.quit()

print(d)
d.to_csv('books.csv')

t1 = time.time()
total_time = t1-t0
print(total_time)
