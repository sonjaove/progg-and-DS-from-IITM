import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None

def analyze_html_structure(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    print("1. Document Title:")
    print(soup.title.string if soup.title else "No title found")
    
    print("\n2. First 500 characters of the HTML:")
    print(html_content[:500])
    
    print("\n3. All script tags:")
    for i, script in enumerate(soup.find_all('script')):
        print(f"Script {i + 1}:")
        print(script.get('src', 'No src attribute'))
        if script.string:
            print(script.string[:100] + "..." if len(script.string) > 100 else script.string)
        print()
    
    print("\n4. Searching for div with class 't':")
    t_divs = soup.find_all('div', class_='t')
    print(f"Number of 't' divs found: {len(t_divs)}")
    if t_divs:
        print("First 't' div content:")
        print(t_divs[0].prettify()[:500])
    
    print("\n5. Searching for div with class 'r':")
    r_divs = soup.find_all('div', class_='r')
    print(f"Number of 'r' divs found: {len(r_divs)}")
    if r_divs:
        print("First 'r' div content:")
        print(r_divs[0].prettify()[:500])
    
    print("\n6. Searching for div with class 'c':")
    c_divs = soup.find_all('div', class_='c')
    print(f"Number of 'c' divs found: {len(c_divs)}")
    if c_divs:
        print("First 'c' div content:")
        print(c_divs[0].prettify()[:500])

def main():
    url = "https://22f3001919.github.io/tds_project_1/"
    html_content = fetch_data(url)
    
    if not html_content:
        return
    
    analyze_html_structure(html_content)

if __name__ == "__main__":
    main()