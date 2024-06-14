# phishing-site-detection-program
> 입력된 URL을 기반으로 피싱 페이지를 감지하는 프로그램

## 소개
랜덤 포레스트 알고리즘을 사용하여 [피싱 웹사이트 데이터셋](https://archive.ics.uci.edu/dataset/327/phishing+websites)에서 제공하는 11가지 주요 특징을 학습시켰습니다. <br/>

### 분석 요소
URL 분석은 HTTP요청, WHOIS, 소켓통신을 통해 분석됩니다.<br/>

1. IP 주소 포함 여부
2. URL 길이
3. HTTPS 토큰
4. 단축 서비스 사용 여부
5. @ 기호 포함 여부
6. SSL 인증서 상태
7. 도메인 등록 기간
8. 도메인 만료일
9. 우클릭 방지
10. 리다이렉션 횟수
11. 포트

모델과 URL을 통해 분석한 결과를 비교하여 피싱 웹사이트 여부를 반환합니다.

<br>

## 화면
**메인화면**

![image](https://github.com/88dldl/phishing-site-detection-program/assets/110217133/d8207b51-1b2b-4a7f-a52c-88c6f58a32d6)

**피싱 검사 - 안전**

![image](https://github.com/88dldl/phishing-site-detection-program/assets/110217133/d08b02fb-be20-4225-87f8-9952539be160)

**피싱 검사 - 위험**

![image](https://github.com/88dldl/phishing-site-detection-program/assets/110217133/302c25b2-46bc-48c5-b0e9-43b8149ecc0c)**
