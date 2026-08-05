import random
import shutil
from pathlib import Path

# ==========================================
# Configuration
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "dataset"

MAX_IMAGES = 300

random.seed(42)

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png")

print("=" * 50)
print("Reducing Dataset")
print("=" * 50)

for class_folder in DATASET_DIR.iterdir():

    if not class_folder.is_dir():
        continue

    images = [
        img for img in class_folder.iterdir()
        if img.suffix.lower() in IMAGE_EXTENSIONS
    ]

    total = len(images)

    if total <= MAX_IMAGES:
        print(f"{class_folder.name:<35} {total} images (Skipped)")
        continue

    random.shuffle(images)

    keep = set(images[:MAX_IMAGES])

    deleted = 0

    for image in images:

        if image not in keep:
            image.unlink()
            deleted += 1

    print(
        f"{class_folder.name:<35}"
        f" Kept: {MAX_IMAGES:<4}"
        f" Deleted: {deleted}"
    )

print("\nDataset reduction completed successfully!")