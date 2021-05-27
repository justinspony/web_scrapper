import urllib.request
import re
import os
from bs4 import BeautifulSoup
import json

"""
Justin Spony
Oct. 2019
"""

if __name__ == '__main__':

    os.chdir(os.path.dirname(__file__))
    title_url_dictionary = {}
    url = "http://www.ucdenver.edu/pages/ucdwelcomepage.aspx"
    request = urllib.request.Request(url)
    html = urllib.request.urlopen(request).read()

    soup = BeautifulSoup(html, 'html.parser')
    main_table = soup.findAll('div', attrs={'id': 'docResponsive'})
    web_scrapper_json = os.getcwd()
    web_scrapper_json += "/web_scrapper.json"

    for link in soup.findAll('a', attrs={'href': re.compile("http")}):
        if type(link.get('title')) is str:
            title_url_dictionary[link.get('title')] = link.get('href')
            print(link.get('title'), link.get('href'))

    print("File will print to:", web_scrapper_json)
    with open(web_scrapper_json, 'w') as outfile:
        json.dump(title_url_dictionary, outfile, indent=4)
