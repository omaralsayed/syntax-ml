import requests 

from bs4 import BeautifulSoup

def url_to_soup(url):
    page = requests.get(url)
    #parse into beautiful soup format 
    to_soup = BeautifulSoup(page.content, 'html.parser')
    return to_soup

def check_mark_in_html(url):
    this_page = requests.get(url)
    if "svg-icon" in page.content:
    return True
    else:
    return False