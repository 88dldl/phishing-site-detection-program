import requests


def get_redirection_count(url):
    try:
        response = requests.head(url, allow_redirects=True)
        redirection_count = len(response.history)
        return redirection_count
    except Exception as e:
        print(f"Error: {e}")
        return 1000


def check_redirection_count(url):
    redirection_count = get_redirection_count(url)
    if redirection_count is not None:
        if redirection_count <= 1:
            return -1
        elif 2 <= redirection_count <= 4:
            return 0
        else:
            return 1
    else:
        return 1


def check_right_click_disabled(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if "event.button==2" in response.text:
                return 1
            else:
                return -1
        else:
            print(f"Error: {response.status_code}")
            return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1


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
