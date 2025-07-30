import requests
from bs4 import BeautifulSoup

def fetch_website_data(url):
    """Fetch the HTML content of a website."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_info(html):
    """Extract information from the HTML content."""
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string if soup.title else 'No title found'
    meta_description = soup.find('meta', attrs={'name': 'description'})
    description = meta_description['content'] if meta_description else 'No description found'
    return title, description

def main():
    url = input("Enter the URL to analyze: ")
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # Ensure the URL has a scheme

    html_data = fetch_website_data(url)
    if html_data:
        title, description = extract_info(html_data)
        print(f"Title: {title}")
        print(f"Description: {description}")

if __name__ == "__main__":
    main()