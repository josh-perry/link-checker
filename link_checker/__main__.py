from bs4 import BeautifulSoup
import argparse
import requests
import re
import time

def check_links(links):
    dead_links = []

    for link in links:
        print(f"Checking '{link}'")
        response = requests.get(link)

        if not response:
            dead_links.append((link, response.status_code))

        time.sleep(1)

    for link in dead_links:
        print(f"Error: '{link[0]}' returned status {link[1]}")

def get_arguments():
    parser = argparse.ArgumentParser(description="A simple link checker for markdown files")
    parser.add_argument("url", type=str, help="The markdown URL to check the links of.")
    return parser.parse_args()

def get_markdown(url):
    response = requests.get(url)
    return response.text

def get_links(markdown):
    pattern = r"\[.+\]\((https?.*?)\)"
    return re.findall(pattern, markdown)

if __name__ == "__main__":
    args = get_arguments()
    markdown = get_markdown(args.url)
    links = get_links(markdown)
    results = check_links(links)
