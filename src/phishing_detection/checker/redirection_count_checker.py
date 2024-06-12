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
