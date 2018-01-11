""" Base script to scrape files from music index directories """
import urllib.request
from bs4 import BeautifulSoup
import subprocess

def tabled(page):
    for item in html.find_all("table"):
        for table in item.find_all("tr"):
            for row in item.find_all("td"):
                for a in row.find_all('a', href=True):
                    #store relative path as 'links' variable
                    links = (a['href'])
                    #concatenate relative link to absolute link
                    final = (source+links)
                    #use wget to download any files stored in a link on requested page
                    subprocess.Popen(['wget', '-i', final])


def listed(page):
    for item in html.find_all("ul"):
        for obj in item.find_all("li"):
            for a in obj.find_all('a', href=True):
                #store relative path as 'links' variable
                links = (a['href'])
                #concatenate relative link to absolute link
                final = (source+links)
                #use wget to download any files stored in a link on requested page
                subprocess.Popen(['wget', '-i', final])



#request the URL of the index from the user
source = input('enter URL: \n')
# read source code of URL
page = urllib.request.urlopen(source).read()
#parse source code of URL
html = BeautifulSoup(page, "html.parser")
#test for structure type
if  html.find_all("table"):
    tabled(page)
elif html.find_all("ul"):
    listed(page)
else:
    print('Structure type of page is unrecognized')
