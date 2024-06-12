import socket
import ssl
from datetime import datetime


def check_ssl_certificate(url):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((url, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=url) as ssock:
                cert = ssock.getpeercert()

        # SSL 인증서의 발급자 확인
        issuer = dict(x[0] for x in cert['issuer'])
        issuer_organization = issuer.get('organizationName', '')

        issuer_organization_lower = issuer_organization.lower()
        trusted_issuer = 'DigiCert' in issuer_organization or \
                         'let\'s encrypt' in issuer_organization_lower or \
                         'comodo' in issuer_organization_lower or \
                         'globalsign' in issuer_organization_lower or \
                         'godaddy' in issuer_organization_lower

        # SSL 인증서의 유효 기간 확인
        not_before = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')
        not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
        validity_period = (not_after - not_before).days

        return trusted_issuer, validity_period

    except Exception as e:
        print(f"SSL 인증서 정보를 가져오는 중 오류 발생: {e}")
        return False, 0  # 기본값 설정


def check_SSLfinal_state(url):
    use_https = url.startswith('https://')
    url_length = len(url)
    if url_length <= 75:
        # www.checktls.com 에서 SSL 인증서 정보 확인
        ssl_url = "www.checktls.com"
        trusted_issuer, validity_period = check_ssl_certificate(ssl_url)
        if use_https:
            if trusted_issuer & validity_period >= 365:
                return -1
            elif trusted_issuer | validity_period < 365:
                return 0
            else:
                return 1
        else:
            return 1
    else:
        return 1