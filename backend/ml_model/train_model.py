import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
import json
import os


# =========================
# Dataset Paths
# =========================

TRAIN_DIR = "../dataset/split_data/train"
VALID_DIR = "../dataset/split_data/valid"


# =========================
# Parameters
# =========================

IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 15


# =========================
# Data Augmentation
# =========================

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=25,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)


valid_datagen = ImageDataGenerator(
    rescale=1./255
)


# =========================
# Load Dataset
# =========================

train_data = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical"
)


valid_data = valid_datagen.flow_from_directory(
    VALID_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical"
)


num_classes = len(train_data.class_indices)

print("Number of Classes:", num_classes)


# =========================
# Save Class Names
# =========================

class_names = list(train_data.class_indices.keys())

with open("class_names.json", "w") as file:
    json.dump(class_names, file, indent=4)

print("Class names saved")


# =========================
# Load MobileNetV2
# =========================

base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)


# Freeze pretrained layers

base_model.trainable = False


# =========================
# Add Custom Classifier
# =========================

x = base_model.output

x = GlobalAveragePooling2D()(x)

x = Dropout(0.4)(x)

output = Dense(
    num_classes,
    activation="softmax"
)(x)


model = Model(
    inputs=base_model.input,
    outputs=output
)


# =========================
# Compile Model
# =========================

model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)


model.summary()


# =========================
# Callbacks
# =========================

callbacks = [

    ModelCheckpoint(
        "best_crop_disease_model.keras",
        monitor="val_accuracy",
        save_best_only=True,
        mode="max",
        verbose=1
    ),


    EarlyStopping(
        monitor="val_loss",
        patience=3,
        restore_best_weights=True
    ),


    ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.2,
        patience=2,
        verbose=1
    )

]


# =========================
# Training
# =========================

history = model.fit(
    train_data,
    validation_data=valid_data,
    epochs=EPOCHS,
    callbacks=callbacks
)


# =========================
# Save Final Model
# =========================

model.save(
    "crop_disease_model.keras"
)


print("\nTraining Completed Successfully!")
print("Model saved as crop_disease_model.keras")