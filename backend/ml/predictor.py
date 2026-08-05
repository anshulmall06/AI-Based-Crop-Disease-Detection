import json
from pathlib import Path

import cv2
import numpy as np
import onnxruntime as ort

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "ml" / "model.onnx"
CLASSES_PATH = BASE_DIR / "ml" / "classes.json"

# Load model
session = ort.InferenceSession(str(MODEL_PATH))

# Load class names
with open(CLASSES_PATH, "r") as f:
    classes = json.load(f)


def preprocess(image_path):
    image = cv2.imread(str(image_path))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = cv2.resize(image, (224, 224))

    image = image.astype(np.float32) / 255.0

    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    std = np.array([0.229, 0.224, 0.225], dtype=np.float32)

    image = (image - mean) / std

    image = np.transpose(image, (2, 0, 1))

    image = np.expand_dims(image, axis=0)

    return image.astype(np.float32)


def predict(image_path):

    image = preprocess(image_path)

    outputs = session.run(
        None,
        {session.get_inputs()[0].name: image}
    )

    output = outputs[0]

    output = output - np.max(output)

    exp_scores = np.exp(output)

    probabilities = exp_scores / np.sum(exp_scores)

    index = np.argmax(probabilities)

    confidence = float(probabilities[0][index])

    return {
        "disease": classes[index],
        "confidence": round(confidence * 100, 2)
    }