# Generic points.
- some internet archives have ***indexed data***, which makes data scraping form the websites very easy and doable on the other hand, there is unindexed datasets, where you have to individually select the attributes you want.

- some pdfs with official data, can also be very structured in and makes their scraping very easy, eg the election result data. 
---
# General procedure:
1. open the wesite, and inspect different elements of it and see where your data lies &rarr; send a GET request to this page, and use ```soup``` to extract the given element &rarr; add a try and except block as well &rarr; you would have to use a loop to extract the entire data, if your data is in multiple pages. &rarr; save the pdf file

2. convert the saved file into txt files (use the xpdf library, command given below)
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

# Excel:
- [using data cleaing using excel](https://youtu.be/7du7xkqeu4s?si=GwTV5RGto-GEBC3F)
    1. you can use `find and replace` (ctrl+H) to replace some of the unwanted texts, or words from any of your data column.
    2. you can also change the data types(data formates) form the home ribbon in excel.

- [Data transformation in Excel](https://youtu.be/gR2IY5Naja0)

- [Convert text-to-columns in Excel (kinda like split function in pyhton)](https://youtu.be/fQeADnqiOAg)

- [Data aggregation in Excel](https://youtu.be/NkpT0dDU8Y4)

- home ribbon &rarr; `find and select` &rarr; `go to special` &rarr; that is where you figure out a empty cell in your entire column and then delete it by right clicking on the selected cells.

- home ribbon &rarr; `conditional formatting` &rarr; fiddle around around with colors and options to get color in your column or data bar &rarr; see the clusters in the data.

------------------------------------------------------------------------------------------------------------------------------------------

# Shell.

- The commands written in shell powerful and fast, and can be parallalized and are pretty popular, and also available in platforms like colab or jyup notebook.

- the commands on the jyup notebook are written with a ! ahead of them. 

- the code has been done on the notes_shell file

- list of commands 
    
```shell
gzip -d data_apr.gz #unzip the data

head -n data_apr #gives the first 5 entries of the file.

wc  data_apr # would give me the 1. total numebr of lines 2. words and chars 

wc -l data_apr #would only give 1. 

# in context to our data, the lines corresponds to number of requests made to the website.
# for getting all the IPs (1st column of the logs) we use the cut command

cut --delimeter " " --fields 1 | head -n 25 #here it is space, and we want first field, and the pipe will pass the output of the first command into the second.

cut --delimeter " " --fields 1 | sort | uniq --count # will count the repeating values of unique ips

#one intresting case comes up while inspecting the logs is that, we see one ip sending about half the total requests (100000), and upon inspecing we find that its prolly a bot, to confirm we use grep

grep "^136.243.228.193" data_apr #grep searches for regular expression - mech of wildcarts to search for content.

#performing the same operation for another ip, which too turns out to be a bot, 


```

- [notebook which does a better job at explaining things.](https://colab.research.google.com/drive/1KSFkQDK0v__XWaAaHKeQuIAwYV0dkTe8)
------------------------------------------------------------------------------------------------------------------------------------------

# text editor 

- ctrl+shift+p - for fomatting a json file, as VS code can identify the formates like these.

- ctrl + d =  multi-select 

- [a brief video](https://youtu.be/99lYu43L9uM?si=c1dEnA7wKx3F8vtF)

------------------------------------------------------------------------------------------------------------------------------------------

# Using OpenRefine.

- the election results problem as seen on the first video on data prepration section, can be solved using open refine, which is an open source software.
    - eg, XYZ and XYZ. Ltd refer to the same company but, a machine would read it as 2 seprate entities.

- this is called *entity resolution* and can be done with the methodoloy of clusturing. (open refine makes it really easy to work with such data)

------------------------------------------------------------------------------------------------------------------------------------------

# Pythonic libraries.
1. `pandas_profiling` library:

    - used essentially for peofiling the data and giving good profile about the data, it generates an html file for a particular dataset 
    ```python
    # to downlaod the library
    pip install pandas_profiling

    #for generating the report.
    from pandas_profiling import ProfileReport 

    prof=ProfileReport(df)
    prof.to_file('report.html')
    files.download('report.html')
    ```

    these lines of code generate a pretty good report of the data at hand, showing correlation b/w the variables and trends in the data and outliers, also gives warnings.

2. `pillow` library:

    - makes the image porcessing easy, just write a script for the images and the changes in the images will be done. 

    - it can also be pretty useful for data visulaization. 
    ```python
    # for installing the library
    pip install Pillow #this does it, but you might need some external libraries as well, incase an error accures during installation.

    from PIL import Image #or any other module you want to exp with.
    
    # Open an image file
    image = Image.open('path/to/image.jpg')

    # Display basic information about the image
    print(f"Image format: {image.format}")
    print(f"Image size: {image.size}")
    print(f"Image mode: {image.mode}")

    # Resize the image
    resized_image = image.resize((800, 600))

    # Save the resized image
    resized_image.save('path/to/resized_image.jpg')

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Save the grayscale image
    grayscale_image.save('path/to/grayscale_image.jpg')

    # Rotate the image by 90 degrees
    rotated_image = image.rotate(90)

    # Save the rotated image
    rotated_image.save('path/to/rotated_image.jpg')
    ```

------------------------------------------------------------------------------------------------------------------------------------------

# References:
- [datacamp tutorials](https://www.datacamp.com/community/tutorials/tutorial-on-scraping-data-from-a-website)
- [geeks for geeks tutorial](https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/)
```python
#comand for converting pdf to txt in python.
pdftotext -layout gujarat-2013.pdf gujarat-2013.txt
```

- [general election parsing colab](https://colab.research.google.com/drive/1SP8yVxzmofQO48-yXF3rujqWk2iM0KSl)

- [one good video](https://youtu.be/dF3zchJJKqk?si=Q1HndBQF06frUqan)

- [cartogram is something very ineresting](https://gramener.com/election/cartogram?ST_NAME=Tamil%20Nadu)

- strucutre of internet logs used here:

    | IP Address  | Identity of the Client (identD) | Username/User ID | Date/Time                      | Request                             | Status Code | Bytes Sent |
    |-------------|---------------------------------|------------------|--------------------------------|-------------------------------------|-------------|------------|
    | 127.0.0.1   | -                               | frank            | [10/Oct/2000:13:55:36 -0700]   | "GET /apache_pb.gif HTTP/1.0"       | 200         | 2326       |

- learn about regular expressions.

- [a small discussion on github about entity resolution.](https://github.com/topics/entity-resolution)

- [Pillow documentation](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html)

- [AirFlow Doc](https://airflow.apache.org/docs/apache-airflow/stable/)