import requests
import os
from bs4 import BeautifulSoup

url = "https://www.jobindex.dk/jobsoegning?q=Python"
page = requests.get(url)

soup  = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="result_list_box")

job_elements = results.find_all("div", class_="PaidJob-inner")

for job_element in job_elements:
    title_elemet = job_element.find("b")
    print(title_elemet.text.strip())

# Link: https://realpython.com/beautiful-soup-web-scraper-python/




#class = PaidJob-inner
#<b>