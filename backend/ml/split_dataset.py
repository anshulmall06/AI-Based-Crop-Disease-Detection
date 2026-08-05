import random
import shutil
from pathlib import Path

# ==========================================================
# Get Backend Folder Automatically
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset Folder
SOURCE_DIR = BASE_DIR / "dataset"

# Output Folder
OUTPUT_DIR = BASE_DIR / "dataset_split"

TRAIN_RATIO = 0.8
RANDOM_SEED = 42

random.seed(RANDOM_SEED)

print(f"Source Folder : {SOURCE_DIR}")
print(f"Output Folder : {OUTPUT_DIR}")

# Check if dataset exists
if not SOURCE_DIR.exists():
    raise FileNotFoundError(f"Dataset folder not found: {SOURCE_DIR}")

# Delete old split if present
if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)

# Create train and test folders
train_dir = OUTPUT_DIR / "train"
test_dir = OUTPUT_DIR / "test"

train_dir.mkdir(parents=True, exist_ok=True)
test_dir.mkdir(parents=True, exist_ok=True)

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png")

print("\nSplitting Dataset...\n")

for class_folder in SOURCE_DIR.iterdir():

    if not class_folder.is_dir():
        continue

    images = [
        img for img in class_folder.iterdir()
        if img.suffix.lower() in IMAGE_EXTENSIONS
    ]

    if len(images) == 0:
        print(f"Skipping {class_folder.name} (No Images)")
        continue

    random.shuffle(images)

    split_index = int(len(images) * TRAIN_RATIO)

    train_images = images[:split_index]
    test_images = images[split_index:]

    train_class_dir = train_dir / class_folder.name
    test_class_dir = test_dir / class_folder.name

    train_class_dir.mkdir(parents=True, exist_ok=True)
    test_class_dir.mkdir(parents=True, exist_ok=True)

    for image in train_images:
        shutil.copy(image, train_class_dir / image.name)

    for image in test_images:
        shutil.copy(image, test_class_dir / image.name)

    print(
        f"{class_folder.name:<35}"
        f" Train : {len(train_images):4}   "
        f"Test : {len(test_images):4}"
    )

print("\n====================================")
print("Dataset Split Completed Successfully")
print("====================================")