import sys
import urllib.error
import urllib.request

from typing import List

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


def get_links(url: str) -> List[str]:
    """Find all links on page at the given url.

    Args:
        url: url of website

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    browser.get(url)
    elements: List[WebElement] = browser.find_elements_by_tag_name("a")
    url_list = []
    for link in elements:
        url = link.get_attribute('href')
        if url is not None:
            url = url.split('#')
            url = url[0].split('?')
            url = url[0]
        url_list.append(url)
    return url_list


def is_valid_url(url: str) -> bool:
    """Check if a url is valid & reachable or not.

    Args:
        url: url of website

    Returns:
        True: if the url is valis and reachable
        False: if the url is unvalid and unreachable or invalid syntax
    """
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        return False
    return True


def invalid_urls(urllist: List[str]) -> List[str]:
    """Validate the urls in urllist and return a new list
    containing the invalid or unreachable urls.

    Args:
        urllist: a list of URLs

    Returns:
        a new list containing only the invalid or unreachable URLs
    """
    invalid_url_list = []
    for url in urllist:
        if not is_valid_url(url):
            invalid_url_list.append(url)
    return invalid_url_list


if __name__ == "__main__":
    browser = webdriver.Chrome('C:\Program Files\Chrome\chromedriver.exe')
    url = sys.argv[1]
    url_list = get_links(url)
    print('These are good links:')
    for url in url_list:
        print(url)
    bad_url = invalid_urls(url_list)
    print('\nThese are bad links:')
    for url in bad_url:
        print(url)
