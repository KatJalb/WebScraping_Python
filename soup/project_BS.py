# We checked robots.txt and we can scap what we wanted

# Librari# Libraries (main)
from tempfile import TemporaryFile
from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

# Additional libraries to make code more functional
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import datetime

# Measuring time of running the program
begin_time = datetime.datetime.now()


######   Additional parameters to specify how many pages to scrap   ######

# Should the number books (each book leading to a separate page with details) be limited to 100?
limit = False 
# How many pages of books (each page is 100 books) to scrap? [Maximum is 100]
pages = 3

if limit == True:
    pages = 1

##############################


######  Generating a list of pages to scrap  #######

# 'Basic' url
url = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page='
links = []

# Loop for more than one page of books to scrap

if limit == False:

    for i in range(1, pages + 1):

        # Accesing the url...
        html = request.urlopen(url)
        bs = BS(html.read(), 'html.parser')

        # ... and finding all pages of books 
        tags = bs.find_all('a', {'class': 'bookTitle'})
        links_i = ['https://www.goodreads.com' + tag['href'] for tag in tags]
        links = links + links_i

##############################

'''
# Access to the "main" site
url = 'https://www.goodreads.com/list/show/1' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

# Finding the links to all sites we want to scrap
tags = bs.find_all('a', {'class': 'bookTitle'})
links = ['https://www.goodreads.com' + tag['href'] for tag in tags]
'''



''' # This code is only used when testing scraping on a single page and was left for easier debugging
d = pd.DataFrame({'title': [], 'author': [], 'year': [], 'publisher': [], 'genre': [], 'pages': [], 'no. of ratings': [], 'rating': []})
links = ['https://www.goodreads.com/book/show/41865.Twilight']
'''


#######  Now we focus on idividual links to book pages  #######

# Creating dataframe to store the data
d = pd.DataFrame({'title': [], 'author': [], 'year': [], 'publisher': [], 'genre': [], 'pages': [], 'no. of ratings': [], 'rating': []})

for link in links:

    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')

    # For each piece of data, we look for certain elements within the HTML code and scrap the text in them
    try:
        title = bs.find('h1', {'id': 'bookTitle'}).text.strip()
    except:
        title = ''
    
    try:
        author = bs.find('a', {'class': 'authorName'}).text.strip()
    except:
        author = ''
    
    try:
        year = bs.find('div', {'id': 'details'}).find_all('div', {'class': 'row'})[1].text.strip()
        year = re.findall('[0-9][0-9][0-9][0-9]', year)[0]
    except:
        year = ''

    try:
        publisher = bs.find('div', {'id': 'details'}).find_all('div', {'class': 'row'})[1].text.strip()
        publisher = re.findall('by.+', publisher)[0][3:]
    except:
        publisher = ''

    try:
        genre = bs.find('a', {'class': 'actionLinkLite bookPageGenreLink'}).text.strip()
    except:
        genre = ''

    try:
        pages = bs.find('div', {'id': 'details'}).find_all('div', {'class': 'row'})[0].text.strip()
        pages = re.findall('([^ \r\n]+) [pP]ages([\r\n]| |$)', pages)[0][0]
    except:
        pages = ''
    
    try:
        no_ratings = bs.find('meta', {'itemprop': 'ratingCount'}).text.split()[0].strip()
    except:
        no_ratings = ''
    
    try:
        rating = bs.find('span', {'itemprop': 'ratingValue'}).text.strip()
    except:
        rating = ''
    
    # We create a dictionary and then add it to the data frame
    book = {'title': title, 'author': author, 'year': year, 'publisher': publisher, 'genre': genre, 'pages': pages, 'no. of ratings': no_ratings, 'rating': rating}
    d = d.append(book, ignore_index = True)

##############################


# We print the obtained dataframe and time it took to scrap and export it to csv   
print(d)
print(datetime.datetime.now() - begin_time)
d.to_csv('BS.csv')

   











es
from tempfile import TemporaryFile
from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)



##### ZAKOMENTOWAĆ JEŚLI POJEDYNCZA STRONA #####

# Access to the "main" site
# Na razie tylko z pierwszej strony
url = 'https://www.goodreads.com/list/show/1' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

# Finding the links to all sites we want to scrap
tags = bs.find_all('a', {'class': 'bookTitle'})
links = ['https://www.goodreads.com' + tag['href'] for tag in tags]

# Creating dataframe for the data
d = pd.DataFrame({'title': [], 'author': [], 'year': [], 'publisher': [], 'genre': [], 'pages': [], 'no. of ratings': [], 'rating': []})

##########


'''
d = pd.DataFrame({'title':[]}) #, 'author':[], 'ISBN':[], 'publication year':[]})
links = ['https://www.goodreads.com/book/show/41865.Twilight']
'''

for link in links:

    # Now we focus on idividual links to book pages
    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')

    try:
        title = bs.find('h1', {'id': 'bookTitle'}).text.strip()
    except:
        title = ''
    
    try:
        author = bs.find('a', {'class': 'authorName'}).text.strip()
    except:
        author = ''
    
    try:
        year = bs.find('div', {'id': 'details'}).find_all('div', {'class': 'row'})[1].text.strip()
        year = re.findall('[0-9]{4}', year)[0]
    except:
        year = ''

    try:
        publisher = bs.find('div', {'id': 'details'}).find_all('div', {'class': 'row'})[1].text.strip()
        publisher = re.findall('by.+', publisher)[0][3:]
    except:
        publisher = ''

    try:
        genre = bs.find('a', {'class': 'actionLinkLite bookPageGenreLink'}).text.strip()
    except:
        genre = ''

    try:
        pages = bs.find('div', {'id': 'details'}).find_all('div', {'class': 'row'})[0].text.strip()
        pages = re.findall('([^ \r\n]+) [pP]ages([\r\n]| |$)', pages)[0][0]
    except:
        pages = ''
    
    try:
        no_ratings = bs.find('meta', {'itemprop': 'ratingCount'}).text.split()[0].strip()
    except:
        no_ratings = ''
    
    try:
        rating = bs.find('span', {'itemprop': 'ratingValue'}).text.strip()
    except:
        rating = ''
    
    book = {'title': title, 'author': author, 'year': year, 'publisher': publisher, 'genre': genre, 'pages': pages, 'no. of ratings': no_ratings, 'rating': rating}
    
    d = d.append(book, ignore_index = True)
    
    print(d)



   











