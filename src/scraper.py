import requests
from bs4 import BeautifulSoup
import re

def scraper(url):
    http_response = requests.get(url)
    soup = BeautifulSoup(http_response.text, 'html.parser')
    
    # Project Gutenberg books have the main content within <body> tags and delimited by the texts below! 5/02/25: "a blessing"
    start_text = "*** START OF THIS PROJECT GUTENBERG EBOOK"
    end_text = "*** END OF THIS PROJECT GUTENBERG EBOOK"
    
    text = soup.get_text()
    start_idx = text.find(start_text)
    end_idx = text.find(end_text)
    
    if start_idx != -1 and end_idx != -1:
        text = text[start_idx:end_idx]
    
    return text

def clean_text(text):
    """
    Cleans the input text by performing the following operations:
    1. Replaces multiple newline characters with a single newline.
    2. Converts all characters to lowercase.
    3. Splits the text into a list of words.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        list: A list of words obtained from the cleaned text.
    """
    text = re.sub(r'\n+', '\n', text) # replace multiple newlines with a single newline. incredible
    text = text.lower()
    words = text.split() # words is a list
    return words