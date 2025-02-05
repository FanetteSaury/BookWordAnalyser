import requests # http requests module
from bs4 import BeautifulSoup # webscraping module
import re # regex module

def scraper(url):
    http_response = requests.get(url)
    soup = BeautifulSoup(http_response.text, 'html')
    txt = soup.get_text()
    return txt

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
    text = re.sub(r'\n+', '\n', text) # replace multiple newlines with a single newline (amazing omg)
    text = text.lower()
    words = text.split() # words is a list
    return words

def counter(text, expression):
    words = clean_text(text)
    histogram = {}

    for w in words:
        histogram[w] = histogram[w] + 1 if w in histogram else 1
    return histogram.get(expression.lower(), 0) # retrieves occurence, 0 otherwise