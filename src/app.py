from flask import Flask, request, jsonify, send_from_directory
from  phishing_detection.detector  import detect_and_alert
from phishing_detection.model_trainer import train_model

app = Flask(__name__)

# 모델 학습
model = train_model()


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    url = data['url']
    result = detect_and_alert(model, url)
    return jsonify({'message': result})


if __name__ == '__main__':
    app.run(debug=True)
