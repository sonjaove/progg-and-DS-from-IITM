import tabula
import requests
import pandas as pd
import os
from bs4 import BeautifulSoup
url='https://www.premierleague.com/publications'
response = requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')
folder_path = r'C:\Users\vvagh\OneDrive - Indian Institute of Science Education and Research Bhopal\Documents\IITM Stuff\programming\TDS_notes\data_sourcing'
for link in soup.select("a[href$='.pdf']"):
    filename = os.path.join(folder_path,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(link['href']).content)
    print(filename)
#then we can use tabula to extract the tables from the pdfs and then use pandas to convert them into dataframes
#the layout of you pdf also matters, if the pdf is not in tabular form then you will have to use OCR to extract the data
#tabula is a tool that can extract tables from pdfs, but it might confues text with tables if the layout is landscape, so you have to carrefully edit it to make it work.