import requests
import re
import json
import pandas as pd
from urllib.parse import urlencode


base_url='https://22f3001919.github.io/tds_project_1/index-BMuYwVbw.html'

st_name='KERALA'

params={
    'st_name':st_name
}
url=f"{base_url}?{urlencode(params)}"

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
    link_df=df[df['ST_NAME'] == 'KERALA']
    #df_k=df[df['AC'] == 'KARUNAGAPALLY']
    #df_k.to_csv('project1_data.csv',index=False)
    #print("sheet saved")
    print(link_df.head())  # Display the first few rows of the DataFrame
else:
    print("JavaScript variable 'const data' not found.")
