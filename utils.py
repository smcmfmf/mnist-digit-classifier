import numpy as np
from PIL import Image, ImageOps


def preprocess_image(file_obj):
    img = Image.open(file_obj).convert("L")  # 그레이스케일
    img = ImageOps.invert(img)
    img = ImageOps.pad(
        img, (28, 28), method=Image.BILINEAR, color=255, centering=(0.5, 0.5)
    )
    arr = np.array(img).astype("float32") / 255.0
    arr = arr.reshape(1, 28, 28, 1)
    return arr


def postprocess(pred):
    """
    모델 예측값(pred)을 받아 JSON으로 반환할 딕셔너리로 후처리합니다.
    """
    # pred는 (10,) 형태의 numpy 배열입니다.
    prob_list = [float(p) for p in pred]  # JSON 직렬화를 위해 python float 리스트로 변환
    prob = float(pred.max())
    cls = int(pred.argmax())
    # 기존 digit, prob 외에 전체 확률 리스트(probabilities)를 추가
    return {"digit": cls, "prob": prob, "probabilities": prob_list}