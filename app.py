import os
import io
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from utils import preprocess_image, postprocess

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        # GPU 메모리 점진적 증가 허용
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print("✅ GPU memory growth enabled")
    except RuntimeError as e:
        print(e)

app = Flask(__name__)

MODEL_PATH = os.environ.get("MODEL_PATH", "model.weights.h5")
print(f"Loading model from {MODEL_PATH} ...")
model = tf.keras.models.load_model(MODEL_PATH)
_ = model.predict(np.zeros((1,28,28,1), dtype=np.float32))

@app.route("/predict", methods=["POST"])
def predict():
    """
    multipart/form-data: file 필드로 이미지 업로드
    """
    if "file" not in request.files:
        return jsonify({"error": "no file"}), 400

    f = request.files["file"]
    arr = preprocess_image(f)  # (1, 28, 28, 1) 형태로 전처리된 이미지
    pred = model.predict(arr, verbose=0)[0]  # shape: (10,)

    # 확률값 정규화 (softmax)
    probs = tf.nn.softmax(pred).numpy()
    digit = int(np.argmax(probs))
    prob = float(probs[digit])

    return jsonify({
        "digit": digit,
        "prob": prob,
        "probs": probs.tolist()
    })


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
