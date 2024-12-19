
import requests
import xml.etree.ElementTree as ET
from langchain.document_loaders import UnstructuredURLLoader


def fetch_sitemap_urls(sitemap_url):
    try:
        # Fetch the sitemap.xml content
        response = requests.get(sitemap_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        
        # Parse the XML content
        root = ET.fromstring(response.content)
        
        # Extract all <loc> elements (URLs)
        urls = [url.text for url in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]        
        return urls
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sitemap: {e}")
        return []
    except ET.ParseError as e:
        print(f"Error parsing sitemap XML: {e}")
        return []
    

def load_data(sitemap_url):
    urls = fetch_sitemap_urls(sitemap_url)
    loaders = UnstructuredURLLoader(urls)
    data = loaders.load()
    return data
