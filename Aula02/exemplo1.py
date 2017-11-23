import requests


def download(url, num_retries=2):
    print('Dowloading: ', url)
    page = None
    try:
        response = requests.get(url)
        page = response.text
    except requests.exceptions.RequestException as e:
        print('Download error: ', e.reason)
    return page


page = download('http://www.google.com')
print(page)
