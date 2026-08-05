import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
from pathlib import Path

# ==========================================
# Paths
# ==========================================
BASE_DIR = Path(__file__).resolve().parent.parent

TRAIN_DIR = BASE_DIR / "dataset_split" / "train"
TEST_DIR = BASE_DIR / "dataset_split" / "test"

# ==========================================
# Hyperparameters
# ==========================================
IMAGE_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 2
LEARNING_RATE = 0.001

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"Using Device : {DEVICE}")

# ==========================================
# Image Transform
# ==========================================
transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )
])

# ==========================================
# Dataset
# ==========================================
train_dataset = datasets.ImageFolder(TRAIN_DIR, transform=transform)
test_dataset = datasets.ImageFolder(TEST_DIR, transform=transform)

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)

print("\nClasses Found:")
print(train_dataset.classes)

NUM_CLASSES = len(train_dataset.classes)

# ==========================================
# Save class names
# ==========================================
import json

with open(BASE_DIR / "ml" / "classes.json","w") as f:
    json.dump(train_dataset.classes,f)

# ==========================================
# Model
# ==========================================
weights = models.ResNet18_Weights.DEFAULT
model = models.resnet18(weights=weights)

for param in model.parameters():
    param.requires_grad = False

model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)

model = model.to(DEVICE)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.fc.parameters(), lr=LEARNING_RATE)

best_accuracy = 0

# ==========================================
# Training
# ==========================================
for epoch in range(EPOCHS):

    model.train()

    running_loss = 0

    for batch_idx, (images, labels) in enumerate(train_loader):

        images = images.to(DEVICE)
        labels = labels.to(DEVICE)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()
        if (batch_idx + 1) % 20 == 0:
            print(
            f"Epoch {epoch+1}/{EPOCHS} | "
            f"Batch {batch_idx+1}/{len(train_loader)} | "
            f"Loss: {loss.item():.4f}"
        )

    # =============================
    # Validation
    # =============================
    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():

        for images, labels in test_loader:

            images = images.to(DEVICE)
            labels = labels.to(DEVICE)

            outputs = model(images)

            _, predicted = torch.max(outputs,1)

            total += labels.size(0)

            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total

    print(
        f"Epoch {epoch+1}/{EPOCHS}"
        f" | Loss : {running_loss:.4f}"
        f" | Accuracy : {accuracy:.2f}%"
    )

    if accuracy > best_accuracy:

        best_accuracy = accuracy

        torch.save(
            model.state_dict(),
            BASE_DIR / "ml" / "best_model.pth"
        )

print("\nTraining Completed")

print(f"Best Accuracy : {best_accuracy:.2f}%")