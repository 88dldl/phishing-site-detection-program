import whois

from src.phishing_detection.checker.Ip_address_checker import check_ip_adderss
from src.phishing_detection.checker.date_checker import check_creation_date, check_expiration_date
from src.phishing_detection.checker.port_open_checker import check_non_standard_ports
from src.phishing_detection.checker.url_checker import check_https_token, check_at_symbol, check_url_length

from src.phishing_detection.checker.redirection_count_checker import check_redirection_count
from src.phishing_detection.checker.right_click_checker import check_right_click_disabled
from src.phishing_detection.checker.shortening_checker import check_shortening
from src.phishing_detection.checker.ssl_certificate_checker import check_ssl_certificate, check_SSLfinal_state


def extract_url_features(url):
    features = []

    # 1. having_IP_Address
    ip_address_check = check_ip_adderss(url)
    features.append(ip_address_check)

    # 2. URL_Length
    url_len_check = check_url_length(len(url))
    features.append(url_len_check)

    # 3. https가 도메인에 있을시
    check_https = check_https_token(url)
    features.append(check_https)

    # 4.Shortening_Service
    shortening = check_shortening(check_https, url)
    features.append(shortening)

    # 5. url 에 @ 포함
    at_in_url = check_at_symbol(url)
    features.append(at_in_url)

    # 6. SSLfinal_State
    sslfinal_state = check_SSLfinal_state(url)
    features.append(sslfinal_state)

    try:
        whois_info = whois.whois(url)
        creation_date = whois_info.get('creation_date', None)
        expiration_date = whois_info.get('expiration_date', None)

        # 7. 도메인 등록 날짜 분석 - 1년 이하일 경우 피싱으로 분류
        check_creation = check_creation_date(creation_date)
        features.append(check_creation)

        # 8. 도메인 만료 날짜 분석(age of domain) - 6개월 이하일시 피싱으로 분류
        check_expiration = check_expiration_date(expiration_date)
        features.append(check_expiration)

    except Exception as e:
        print(f"WHOIS 조회 중 오류 발생: {e}")
        features.append(1)
        features.append(1)

    # 9. 우클릭 비허용
    right_click_disabled = check_right_click_disabled(url)
    features.append(right_click_disabled)

    # 10. 리다이렉션 횟수
    redirection_count = check_redirection_count(url)
    features.append(redirection_count)

    #11. 비표준 포트 열림 확인
    non_standard = check_non_standard_ports(url)
    features.append(non_standard)

    return features
