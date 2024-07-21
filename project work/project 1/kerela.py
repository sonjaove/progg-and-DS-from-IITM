import requests
import re
import json
import pandas as pd
from urllib.parse import urlencode

def get_urls(base_url, st_name):
    params = {
        'st_name': st_name
    }
    url = f"{base_url}?{urlencode(params)}"
    
    # Step 1: Fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.text
    
    # Step 2: Extract the JavaScript variable `const data` from the HTML
    pattern = re.compile(r'const data = (\[.*?\]);', re.DOTALL)
    match = pattern.search(html_content)
    
    if match:
        json_data = match.group(1)
        # Step 3: Convert the extracted JSON data into a pandas DataFrame
        data_list = json.loads(json_data)
        df = pd.DataFrame(data_list)
        link_df = df[df['ST_NAME'] == st_name]
        
        return link_df['link'].tolist()
        
    else:
        print("JavaScript variable 'const data' not found.")

def get_data(endpoints):
    urls = [f"https://22f3001919.github.io/tds_project_1/{endpoint}" for endpoint in endpoints]
    all_data = []
    for url in urls:
        response = requests.get(url)
        html_content = response.text
        pattern = re.compile(r'const data = (\[.*?\]);', re.DOTALL)
        match = pattern.search(html_content)
        if match:
            json_data = match.group(1)
            data = json.loads(json_data)
            all_data.extend(data)
        else:
            print("JavaScript variable 'const data' not found.")
    
    df = pd.DataFrame(all_data)
    return df

def save_data(df, filename, filename2, ac_name='KARUNAGAPALLY'):
    # Save data for the entire state
    df.to_csv(filename, index=False)
    
    # Filter and save data for the specific AC
    df_ac = df[df['AC'].str.contains(ac_name, case=False, na=False)]
    df_ac.to_csv(filename2, index=False)
    
    print(f"Data for the entire state saved to {filename}")
    print(f"Data for {ac_name} saved to {filename2}")

if __name__ == '__main__':
    base_url = 'https://22f3001919.github.io/tds_project_1/index-BMuYwVbw.html'
    st_name = 'KERALA'
    urls = get_urls(base_url, st_name)
    df = get_data(urls)
    save_data(df, 'project1_data.csv', 'project1_data_karunagapally.csv')