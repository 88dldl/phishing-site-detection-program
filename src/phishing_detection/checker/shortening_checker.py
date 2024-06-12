import requests


def check_shortening(check_https, url):
    url_length = len(url)
    if check_https == 1:
        return 1
    else:
        if url_length <= 75:
            response = requests.head(url, allow_redirects=True)
            if response.url != url:
                return 1
            else:
                return -1
        else:
            return -1
