import re


def check_ip_adderss(url):
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    if re.search(ip_pattern, url):
        return 1
    else:
        return -1


def check_https_token(url):
    domain_start = url.find('://') + 3
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    if "https" in domain:
        return 1
    else:
        return -1


def check_at_symbol(url):
    if "@" in url:
        return 1
    else:
        return -1


def check_url_length(url_length):
    if url_length < 54:
        return 1
    elif 54 <= url_length <= 75:
        return 0
    else:
        return -1
