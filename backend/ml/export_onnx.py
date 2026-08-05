import json
from pathlib import Path

import torch
import torch.nn as nn
from torchvision import models

# ==========================================
# Paths
# ==========================================
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "ml" / "best_model.pth"
ONNX_PATH = BASE_DIR / "ml" / "model.onnx"
CLASSES_PATH = BASE_DIR / "ml" / "classes.json"

# ==========================================
# Load Classes
# ==========================================
with open(CLASSES_PATH, "r") as f:
    classes = json.load(f)

NUM_CLASSES = len(classes)

# ==========================================
# Build Model
# ==========================================
model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)

model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
model.eval()

# ==========================================
# Dummy Input
# ==========================================
dummy_input = torch.randn(1, 3, 224, 224)

# ==========================================
# Export
# ==========================================
torch.onnx.export(
    model,
    dummy_input,
    ONNX_PATH,
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={
        "input": {0: "batch_size"},
        "output": {0: "batch_size"},
    },
    opset_version=17,
)

print("ONNX model exported successfully!")
print("Saved to:", ONNX_PATH)