'''requests library is used to send HTTP requests to the server and the html code is parsed using BeautifulSoup, some other libraries used are:
json, re, os, sys, time, datetime, argparse, urllib, urllib3, requests, bs4, and lxml.
json stands for JavaScript Object Notation, it is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. 
this the simlpest way to get the data of the desired city, by simply copy pasting the url='https://www.bbc.com/weather/2643743' of that city, in this case bhopal
and then call the get function of the requests library to get the data of the city.
'''

import requests
import json
import re
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

# Define the request city
req_city = 'bhopal'

# Create the API URL with the correct parameters
api_key = 'e77044246c444d5f9b872624241906'
base_url = 'http://api.weatherapi.com/v1/current.json'
params = {
    'key': api_key,
    'q': req_city
}

# Construct the full URL
loc_url = f"{base_url}?{urlencode(params)}"

# Make the request
res = requests.get(loc_url)

# Debugging: Print the URL and response status
print(f"Request URL: {loc_url}")
print(f"Response Status Code: {res.status_code}")

# Check if the response is successful
if res.status_code == 200:
    try:
        # Parse the JSON response
        data = pd.DataFrame(res.json())
        print(data)
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print("Response content:", res.text)
else:
    print(f"Failed to retrieve data: {res.status_code}")
    print("Response content:", res.text)
