from scraper import scraper, clean_text
import re
import matplotlib.pyplot as plt
import heapq
from collections import defaultdict # provides default nonexistent key replacement. Set to 0.
from typing import List, Dict, Tuple

def count_word_frequencies(words: List[str]) -> Dict[str, int]:
    """Counts the frequency of each word in the list."""
    word_histogram = defaultdict(int)
    for word in words:
        word_histogram[word] += 1
    return word_histogram

def get_top_10_words(word_histogram: Dict[str, int]) -> List[Tuple[str, int]]:
    """Retrieves the top 10 most frequent words."""
    return heapq.nlargest(10, word_histogram.items(), key=lambda item: item[1])

def plot_top_10(word_histogram: Dict[str, int], expression: str) -> None:
    """Plots the top 10 most frequent words and highlights the searched expression."""
    top_words = get_top_10_words(word_histogram)
    if expression not in dict(top_words):
        top_words.append((expression, word_histogram.get(expression, 0)))
    top_words = sorted(top_words, key=lambda item: item[1], reverse=True)
    words, occurrences = zip(*top_words)
    plt.figure(figsize=(12, 6))
    colors = ['red' if word == expression else 'blue' for word in words]
    plt.bar(words, occurrences, color=colors)
    plt.xlabel('Words')
    plt.ylabel('Occurrences')
    plt.title(f'Top 10 Words by number of occurences vs {expression}')
    plt.xticks(rotation=45)
    plt.savefig(f"demonstration_charts/BookWordAnalyser_{expression}.png")

if __name__ == "__main__":
    url = input("Enter the URL of the novel (or type 'test' to use a default URL): ")
    if url.lower() == "test":
        url = "https://www.gutenberg.org/cache/epub/84/pg84-images.html"
    text = scraper(url)
    expression = input("Enter the expression to search for: ")
    words = clean_text(text)
    word_histogram = count_word_frequencies(words)
    occurrences = word_histogram.get(expression.lower(), 0)
    print(f'The expression "{expression}" occurs {occurrences} times in the novel.')
    plot_top_10(word_histogram, expression.lower())