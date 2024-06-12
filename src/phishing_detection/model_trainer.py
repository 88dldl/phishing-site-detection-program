import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train_model():
    # 비정상 URL 데이터 셋
    file_path = 'data/findata.csv'
    data = pd.read_csv(file_path, header=None)

    # 데이터의 특징과 레이블로 나누기
    x = data.iloc[:, :]  # 마지막 열을 제외한 모든 열을 특징으로 사용
    y = data.iloc[:, -1]  # 마지막 열을 레이블로 사용

    # 학습 데이터와 테스트 데이터로 분할
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # 모델 초기화
    model = RandomForestClassifier(n_estimators=x.shape[1], random_state=42)

    # 모델 학습
    model.fit(x_train, y_train)


    # 테스트 데이터로 예측
    y_pred = model.predict(x_test)

    # 정확도 평가
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')

    return model
