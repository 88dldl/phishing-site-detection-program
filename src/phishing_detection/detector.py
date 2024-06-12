from src.phishing_detection.url_features_extractor import extract_url_features


def detect_and_alert(model, url):
    url_features = extract_url_features(url)
    prediction = model.predict([url_features])
    if prediction[0] == 1:
        return "경고: 이 URL은 피싱 사이트로 의심됩니다."
    else:
        return "이 URL은 안전한 것으로 판단됩니다."
