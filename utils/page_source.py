import requests

def get_page_source(url):
    response = requests.get(url)
    return response.text