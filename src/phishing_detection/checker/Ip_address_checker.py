import re


def check_ip_adderss(url):
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    if re.search(ip_pattern, url):
        return 1
    else:
        return -1
