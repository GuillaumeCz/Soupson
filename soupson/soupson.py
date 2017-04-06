#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup
import argparse

print "Bonjour ! Voici les soupes de la semaine :"

def display_menu(url="fr", filename=None):

    soup = BeautifulSoup(requests.get(url).text, "lxml")

    menu = ""
    for row in soup.find_all("div", class_="entry-content")[0].find_all("p")[1:]:
        menu += row.string + "\n"

    if filename is not None:
        f1=open('./' + filename, 'w+')
        f1.write(menu)
    else:
        print menu

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-l","--language" ,help="Language to display")
    parser.add_argument("-f", "--filename", help="output file")
    args = parser.parse_args()

    if args.language is not None:
        if args.language == "eng":
            url =  "http://www.soupson.ca/?lang=en"
        elif args.language == "fr":
            url =  "http://www.soupson.ca"
        display_menu(url, args.filename)

if __name__ == '__main__':
    main()
