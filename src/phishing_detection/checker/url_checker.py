def check_https_token(url):
    # URL에서 도메인 부분 추출
    domain_start = url.find('://') + 3  # "://" 이후부터 체크
    domain_end = url.find('/', domain_start)  # 다음 슬래시("/") 전까지
    if domain_end == -1:  # 슬래시가 없는 경우
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # 도메인 부분에 "https" 토큰의 존재 여부 확인
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
