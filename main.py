import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import ssl
import subprocess
import os
import pathlib

def image_scrape(url, file_type, folder):
        extension = file_type
        i = 1
        filename = folder + extension
        r = requests.get(url)
        with open(filename, 'wb') as outfile:
            outfile.write(r.content)

def create_directory(folder):
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
    except OSError:
        print("error creating a folder")
        #error message is as horrible as i could think of so there is motivation to not make mistakes
        raise


ua = UserAgent(verify_ssl=False)
url = input("Input url to the album")
response = requests.get(url, headers={'User-Agent':ua.chrome})
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find(id="title")
print("Title of the album: " + title.text)
create_directory(title.text.strip());
links = soup.find_all("a", class_="image")
i = 0
for link in links:
    print(link)
    try:
        if '.png' in link['href']:
            extension = '.png'
        elif '.jpg' in link['href'] or '.jpeg' in link['href']:
            extension = '.jpeg'
        elif '.gif' in link['href']:
            extension = '.gif'
        else:
            extension = ".jpg"
        i += 1
        folder = title.text.strip() +"/" + str(i)
        image_scrape(link['href'], extension, folder)
    except ValueError:
            pass

