import socket
from urllib.parse import urlparse


def check_non_standard_ports(url):
    non_standard_ports = [21, 22, 445, 1433, 1521, 3306, 3389]
    # URL에서 호스트 이름 추출
    hostname = url.split('//')[-1].split('/')[0]

    for port in non_standard_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # 타임아웃 설정
            try:
                result = sock.connect_ex((hostname, port))
                if result == 0:
                    return 1
            except (socket.gaierror, socket.timeout, socket.error) :
                return 1
    return -1
