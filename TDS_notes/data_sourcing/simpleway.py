import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.bbc.com/weather/1275841' # current weather conditions for bhopal.
response = requests.get(url)

print(f"Request URL: {url}")
print(f"Response Status Code: {response.status_code}")

# Check if the response is successful
if response.status_code == 200:
    try:
        # Parse the HTML response
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract relevant data
        # Note: You will need to inspect the HTML structure of the page to locate the specific data you need
        location = soup.find('h1', class_='wr-c-location__name').text.strip()
        temperature = soup.find('span', class_='wr-value--temperature--c').text.strip()
        description = soup.find('div', class_='wr-day__weather-type-description').text.strip()
        
        # Create a DataFrame
        data = {
            'Location': [location],
            'Temperature': [temperature],
            'Description': [description]
        }
        
        df = pd.DataFrame(data)
        print(df)
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print("Response content:", response.text)
