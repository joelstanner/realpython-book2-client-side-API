from bs4 import BeautifulSoup
import requests


# response is our requests object.  Get the text and make a soup object
response = requests.get('http://www.web2py.com/')

html_text = response.text

soup = BeautifulSoup(html_text)

links = soup.find_all('a')

# grab all of the <a> tags and print the URL
for a in links:
    print a.get('href'), "-----", a.get_text()