# 🖋️ MNIST 숫자 예측 시스템
이 프로젝트는 MNIST 데이터셋을 사용하여 숫자를 인식하는 딥러닝 모델을 사전 학습시킨 뒤 사용자가 숫자를 그리면 이를 예측하는 프로젝트입니다.

# 📋 프로젝트 개요
```
모델: TensorFlow/Keras로 구현된 CNN(합성곱 신경망)을 사용하여 MNIST 손글씨 숫자를 분류합니다.
학습: train.py 스크립트를 통해 모델을 학습시키고, 학습된 가중치를 model.weights.h5 파일로 저장합니다.
웹 앱: app.py (Flask)를 실행하면 로컬 서버가 열립니다. 사용자는 웹 브라우저의 캔버스에 숫자를 그릴 수 있으며, "Predict" 버튼을 누르면 모델이 예측한 결과를 즉시 보여줍니다.
```

# 🧰 기술 스택
```Backend: Python, Flask
Deep Learning: TensorFlow / Keras
Data Handling: NumPy
학습 시각화: Matplotlib
Frontend: HTML, CSS, JavaScript (with HTML Canvas)
```

# 📁 레포지토리 구조
```.
├── app.py              # Flask 웹 애플리케이션 실행 파일
├── train.py            # 모델 학습 스크립트
├── utils.py            # 모델 구조(build_model) 및 데이터 로드(load_mnist) 헬퍼 함수
├── model.weights.h5    # (train.py 실행 후 생성) 최종 학습된 모델 가중치
├── checkpoints/        # 학습 중 저장되는 모델 체크포인트
│   └── best.weights.h5
├── history.png         # (train.py 실행 후 생성) 학습/검증 손실 및 정확도 그래프
├── templates/
│   └── index.html      # 웹페이지 HTML (그리기 캔버스 포함)
├── static/
│   └── style.css       # 웹페이지 CSS 스타일
└── README.md           # 프로젝트 요약
```
# 🛠️ 설치 방법
## 1. 레포지토리 복제:
```
Bash

git clone [https://github.com/smcmfmf/mnist-digit-classifier.git]
cd mnist-digit-classifier
```

## 2. (권장) 가상 환경 생성 및 활성화:
```
Bash

python -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows
```

## 3. 의존성 패키지 설치: (이 프로젝트의 필수 패키지 입니다.)
```
Bash

pip install tensorflow flask numpy matplotlib
```

# 🚀 사용 방법

## 1단계: 모델 학습
```
먼저 train.py를 실행하여 MNIST 데이터로 CNN 모델을 학습시킵니다.

1. MNIST 데이터를 자동으로 다운로드합니다.

2. 학습을 진행하면서 checkpoints/best.weights.h5 경로에 최적의 가중치를 저장합니다.

3. 이후 더이상의 학습으로 모델의 정확도가 변화하지 않을 경우 EarlyStopping를 사용하여
checkpoints/best.weights.h5에 최적의 가중치를 가진 모델을 저장합니다.

4. 학습 과정 동안의 모델의 정확도와 손실률의 추이를 보여주는 history.png가 저장되고,
사용자에게 그래프로 출력됩니다.
```

## 2단계: 웹 애플리케이션 실행
```
app.py를 실행하여 Flask 서버를 실행합니다.

1. 서버가 실행되면 터미널에 다음과 같은 메시지가 나타납니다.

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## 3단계: 숫자 예측하기
```
웹 브라우저를 열고 http://127.0.0.1:5000/ 주소로 이동합니다.

1. 웹 브라우저의 주소창에 http://127.0.0.1:5000/이나 localhost:5000/을 입력합니다.

2. 숫자를 작성하는 캔버스에 마우스로 0 ~ 9까지의 숫자를 중앙부분에 맞추어 그립니다.

3. 예측 버튼을 누르면 모델이 예측한 숫자와 각 숫자 클래스별 예측 확률 그래프가 표시됩니다.

4. 지우기 버튼을 눌러 캔버스를 초기화할 수 있습니다.
```
