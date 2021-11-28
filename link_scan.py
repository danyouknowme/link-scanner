import sys
from typing import List
from selenium import webdriver


def get_links(url: str) -> List[str]:
    """Find all links on page at the given url.

    Args:
        url: url of website

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    browser.get(url)
    elements = browser.find_elements_by_tag_name("a")
    url_list = []
    for link in elements:
        url = link.get_attribute('href')
        if url is not None: 
            url = url.split('#')
            url = url[0].split('?')
            url = url[0]
        url_list.append(url)
    return url_list


if __name__ == "__main__":
    browser = webdriver.Chrome('C:\Program Files\Chrome\chromedriver.exe')
    url = sys.argv[1]
    url_list = get_links(url)
    print('These are good links:')
    for url in url_list:
        print(url)

