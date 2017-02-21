#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup

"""
Gros test avec GIT

"""

print "Bonjour ! Voici les soupes de la semaine :"

if len(sys.argv)>1:
	arg = sys.argv[1] 
	if  arg == "eng":
		url =  "http://www.soupson.ca/?lang=en"
	elif arg == "fr":
		url = "http://www.soupson.ca"

soup = BeautifulSoup(requests.get(url).text, "lxml")

menu = ""
for row in soup.find_all("div", class_="entry-content")[0].find_all("p")[1:]:
    menu += row.string + "\n"

if len(sys.argv) > 2:
    f1=open('./' + sys.argv[2], 'w+')
    f1.write(menu)
else:
    print menu
