import os
import requests
import subprocess
from bs4 import BeautifulSoup
import shutil
import base64

url = "https://bones.fandom.com/wiki/Bones_Wiki"
page = requests.get(url); # henter alt på siden
text = page.text

soup = BeautifulSoup(page.content, "html.parser")

#---------- images ---------

image_list = []

results = soup.find(id = "gallery-0")

images = results.find_all("div", class_="gallery-image-wrapper accent")

for image in images:
    images01 = image.find_all('img', class_="thumbimage lazyload")
    
    for i in images01:
        data_src = i['data-src']
        data_src_splited = data_src.split('/revision', 1)[0]

    image_list.append(data_src_splited)

os.mkdir("src")
os.chdir("src")

count = 0

for i in image_list:
    
    count = count + 1

    req = requests.get(i, stream=True)

    with open(f'image{count}{i[-4:]}', 'wb') as f:
        for chuck in req:
            f.write(chuck)

os.chdir('..')

with open('index.html', 'w', encoding="utf-8") as f:
    f.write(text)

webbrowser.open("index.html");






    




    




        


# https://static.wikia.nocookie.net/bones/images/e/e1/1x06.jpg



