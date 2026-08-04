import os
import shutil
import random
from sklearn.model_selection import train_test_split

SOURCE_DIR = "../dataset/PlantVillage"
OUTPUT_DIR = "../dataset/split_data"

TRAIN_RATIO = 0.8
VALID_RATIO = 0.1
TEST_RATIO = 0.1


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


classes = os.listdir(SOURCE_DIR)

print("Total Classes:", len(classes))


for class_name in classes:

    class_path = os.path.join(SOURCE_DIR, class_name)

    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)

    print(f"{class_name}: {len(images)} images")

    train_images, temp_images = train_test_split(
        images,
        test_size=0.2,
        random_state=42
    )

    valid_images, test_images = train_test_split(
        temp_images,
        test_size=0.5,
        random_state=42
    )


    for folder, image_list in [
        ("train", train_images),
        ("valid", valid_images),
        ("test", test_images)
    ]:

        destination = os.path.join(
            OUTPUT_DIR,
            folder,
            class_name
        )

        create_folder(destination)

        for image in image_list:

            source_file = os.path.join(
                class_path,
                image
            )

            destination_file = os.path.join(
                destination,
                image
            )

            shutil.copy(
                source_file,
                destination_file
            )


print("Dataset splitting completed successfully!")