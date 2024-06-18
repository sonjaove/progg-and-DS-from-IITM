- different types of data files:

1. **.tsv.gz** - tab seprated values.
2. **.csv** - comma seprated value.
3. **.xls** 
4. **.excel**
5. **.shp**
6. **.xml**
etc........

- **beautiful soup** is one of the python library used to **scrape** data from the web 

    a sample code with beautiful soup 

```python
pip install beautifulsoup4 requests

        import requests
        from bs4 import BeautifulSoup
        # URL of the page to scrape
        url = 'https://example.com'
        # Send a GET request to the webpage
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find and print the title of the page
            title = soup.title.string
            print('Page Title:', title)
            # Find and print all the hyperlinks on the page
            for link in soup.find_all('a'):
                print('Link:', link.get('href'))
            # Find and print all the paragraphs on the page
            for paragraph in soup.find_all('p'):
                print('Paragraph:', paragraph.text)
        else:
            print(f'Failed to retrieve the page. Status code: {response.status_code}')
```

# Methods of getting data

1. **Download** the data.
2. **Query** the data from somewhere, i.e the process of requesting specific information from a database or dataset via a query language or an API or is available via a library.
3. **Scrape** it from somehwere (brute froce only done when above 2 methods fail) i.e It's not directly available in a convenient form that you can query or download,  It's available on a PDF file. It's available in a Word document. It's available on an Excel file. It's kind of structured, but you will have to figure out that structure and extract it from there.

# Scrapping with 

## 1. Excel:

- use the query feature availbale in the data tab of excel
     ![alt text](image.png)

     - eg
        
        [importing data in excel by creating a query](https://youtu.be/OCl6UdpmzRQ?si=XiIRU0ipxM4sf2-R)

## 2. Google sheets:

- these foemulas will be live formulas, i.e if you refresh the page, the data imported as well will eb refreshed.

- `importhtml` is used in google sheets, which accepts the following parameter:
    1. url - the url from where the data is to be loaded

    2. query - either a list or table depending on what type of structure contains the desired data.

    3. num - the number of table on that web page 

    - the output here will be the result of a formula, so you might wanna paste it on the workbook, and then strat editin the result.

- `importxml` is another live formula for getting structured data, the fromates permitted are, XML, HTML, CSV, TSV, RSS and ATOM XML feeds.

- `importrange` range of cells from a specified spreadsheet

- `importfeed` imports RSS or ATOM feed.

- `importdata` imports data at a given url in **.csv** formate.