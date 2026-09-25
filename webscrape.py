import requests
from bs4 import  BeautifulSoup
import numpy as np
import pandas as pd

url = 'https://www.example.com/data'

def download(url,filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

def parse_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    return soup 

download(url, 'data.html')
soup = parse_html('data.html')

title = soup.title
