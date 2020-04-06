import requests
from bs4 import BeautifulSoup

class HTMLUtil:
    def fetch_data(self, url: str, tag: str = None, class_name: str = None) -> str:
        """Fetch whole HTML document, or extract only given elements."""
        if class_name == None and tag == None:
            return requests.get(url).text
        else:
            html_data = requests.get(url).text
            soup = BeautifulSoup(html_data, 'html.parser')

            return soup.find_all(tag, class_=class_name)
