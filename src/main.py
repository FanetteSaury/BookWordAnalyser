from scraper import *
import re

if __name__ == "__main__":
    url = input("Enter the URL of the novel: ")
    text = scraper(url)
    
    expression = input("Enter the expression to search for: ")  # User input for the expression
    occurrences = counter(text, expression)
    
    print(f'The expression "{expression}" occurs {occurrences} times in the novel.')