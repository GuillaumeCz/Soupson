#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup
import argparse


def display_menu(lang="fr", filename=None):

    if lang == "fr":
        url = "http://www.soupson.ca"
        print "Bonjour ! Voici les soupes de la semaine :\n\n"
    elif lang == "eng":
        url = "http://www.soupson.ca?lang=en"
        print "Hello ! This week's soups are :\n\n"
      
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
    parser.add_argument("-l","--language" ,help="Language to display ['eng' or 'fr']")
    parser.add_argument("-f", "--filename", help="output file")
    args = parser.parse_args()
    if args.language is not None:
        display_menu(args.language,args.filename)
    else:
        display_menu(filename=args.filename)

if __name__ == '__main__':
    main()
