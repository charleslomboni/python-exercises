import requests
import re
from bs4 import BeautifulSoup

HTML_FILE_NAME = 'html_page.html'

def handle_html_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(str(content))


def scraper_page(url_wiki):

    response = requests.get(url_wiki)

    if (response.status_code != 200):
        print(f'Error to retrieve data from the page. Status code: {response.status_code}')
    else:
        soup = BeautifulSoup(response.content, "html.parser")
        for infobox_class in soup.find_all('table', class_ = "infobox vcard"):
            complete_html = str(infobox_class).replace('//', 'http://').replace('/wiki/', 'https://en.wikipedia.org/wiki/')
            handle_html_file(HTML_FILE_NAME, complete_html)


if __name__ == '__main__':
    scraper_page('https://en.wikipedia.org/wiki/Roger_Federer')