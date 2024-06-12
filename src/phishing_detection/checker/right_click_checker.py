import requests


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
