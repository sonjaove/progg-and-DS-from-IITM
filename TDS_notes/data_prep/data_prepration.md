# Generic points.
- some websites such as 

    👉 https://www.ncei.noaa.gov/data/precipitation-persiann/access/

    have ***indexed data***, which makes data scraping form the websites very easy and doable on the other hand, there is unindexed datasets, where you have to individually select the attributes you want.

- some pdfs with official data, can also be very structured in and makes their scraping very easy, eg the election result data. 

# General procedure:
1. open the wesite, and inspect different elements of it and see where your data lies &rarr; send a GET request to this page, and use soup to extract the given element &rarr; add a try and except block as well &rarr; you would have to use a loop to extract the entire data, if your data is in multiple pages. &rarr; save the pdf file

2. convert the saved file into txt files (use the xpdf library, command given below) &rarr; 
# Tools:
- **BeautifulSoup** is a python library that is used to scrape data from websites, it creates a parse tree for parsing HTML and XML documents.
- **requests** is a python library that is used to send HTTP requests.
- **pandas** is a python library that is used to store data in a dataframe.
- **selenium** is a python library that is used to automate web browsers, it is useful when the data is in the form of a table and the table is dynamic, i.e. the table is not loaded at the initial stage, but is loaded when you scroll down.

# Example: 
- scraping a table from a website:
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/population-by-country/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))[0]
df.to_csv('population.csv')
```
------------------------------------------------------------------------------------------------------------------------------------------

# References:
- [datacamp tutorials](https://www.datacamp.com/community/tutorials/tutorial-on-scraping-data-from-a-website)
- [geeks for geeks tutorial](https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/)
```python
#comand for converting pdf to txt
pdftotext -layout gujarat-2013.pdf gujarat-2013.txt
```

- [general election parsing colab](https://colab.research.google.com/drive/1SP8yVxzmofQO48-yXF3rujqWk2iM0KSl)

