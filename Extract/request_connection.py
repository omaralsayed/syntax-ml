import requests 
from bs4 import BeautifulSoup

def url_to_soup(url):
    page = requests.get(url)
    #parse into beautiful soup format 
    to_soup = BeautifulSoup(page.content, 'html.parser')
    return to_soup

def top_answers_stackoverflow(inp):
    str_input = inp.split() 
    url_query = "https://stackoverflow.com/search?q="

    for ii in str_input:
        url_query += str_input[ii]
        url_query += '+'


   # to_soup = url_to_soup('https://stackoverflow.com/search?q=python+reverse+list')
    # starting to sift through the search results 

    # finding all of the search results
    answers = url_query.find_all("div", {"class":"question-summary search-result"})#find all 

    # checking for the conditions of if answered, if answered go to url and check for green check and code 

    a_i = 0

    for answer in answers:
        a_i += 1
        if a_i == 4:
            break
        # if there are answers check each webpage for check mark and if there's a code block
        # opening web page to check 
        link_find = answer.find("a", {"class":"question-hyperlink"})
        link = 'https://stackoverflow.com/' + link_find['href']
        print("Querying link: {}".format(link))

        answer_soup = url_to_soup(link)

        # find check mark 
        checked = answer_soup.find("div", {"class":"accepted-answer"})
        #print(checked)
        if checked != None:
            code = checked.find("div", {"class":"post-text"})
            code_samples = code.findAll("code")
            for code in code_samples:
                print(code.prettify())
        else:
            continue
    return "here's the top code sample"
        