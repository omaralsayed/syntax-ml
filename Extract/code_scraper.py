import requests 
from bs4 import BeautifulSoup
from WEB_SCRAPE_FUNCS import url_to_soup

# import url from request_connection.py
soup = url_to_soup('https://stackoverflow.com/questions/16605362/in-bash-you-can-set-x-to-enable-debugging-is-there-any-way-to-know-if-that-has')

# check for <code> tags in the html
code = soup.findAll("code")
print(code)