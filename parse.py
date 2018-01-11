""" Base script to scrape files from music index directories """
import urllib.request
from bs4 import BeautifulSoup
import subprocess

#request the URL of the index from the user
source = input('enter URL: \n')

# read source code of URL
page = urllib.request.urlopen(source).read()

# parse out nested list tags
html = BeautifulSoup(page, "html.parser")
for item in html.find_all("ul"):
    for obj in item.find_all("li"):
        for a in obj.find_all('a', href=True):
            #store relative path as 'links' variable
            links = (a['href'])
            #concatenate relative link to absolute link
            final = (source+links)
            #use wget to download any files stored in a link on requested page
            subprocess.Popen(['wget', '-i', final])
