import time

from src.phishing_detection.url_features_extractor import extract_url_features


def detect_and_alert(model, url):
    start_time = time.time()  # 시작 시간 기록

    url_features = extract_url_features(url)
    prediction = model.predict([url_features])

    end_time = time.time()  # 종료 시간 기록
    elapsed_time = end_time - start_time  # 실행 시간 계산
    print(f"실행 시간: {elapsed_time}초")

    if prediction[0] == 1:
        return "경고: 이 URL은 피싱 사이트로 의심됩니다."
    else:
        return "이 URL은 안전한 것으로 판단됩니다."
