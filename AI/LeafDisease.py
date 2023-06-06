import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import joblib

# Step 1: Dataset Collection

# TODO: Collect the dataset of fruit tree and vegetable plant leaf images

# Step 2: Data Preprocessing

# Define the directories for the dataset
train_dir = "Images"
test_dir = "Images"

# Preprocess the images and generate batches of augmented data
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
)
test_datagen = ImageDataGenerator(rescale=1.0 / 255)

# Generate the training and testing datasets
train_dataset = train_datagen.flow_from_directory(
    train_dir, target_size=(150, 150), batch_size=32, class_mode="binary"
)
test_dataset = test_datagen.flow_from_directory(
    test_dir, target_size=(150, 150), batch_size=32, class_mode="binary"
)

# Step 3: Model Selection

# Define the CNN model
model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Conv2D(
            32, (3, 3), activation="relu", input_shape=(150, 150, 3)
        ),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(128, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid"),
    ]
)

# Compile the model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Step 4: Model Training

# Train the model
model.fit(train_dataset, epochs=1, validation_data=test_dataset)

# Step 5: Model Evaluation

# Evaluate the model on the testing dataset
loss, accuracy = model.evaluate(test_dataset)
print(f"Test loss: {loss}")
print(f"Test accuracy: {accuracy}")

# Step 6: Deployment
joblib.dump(model, "trained_model.pkl")
# TODO: Deploy the model in an application or create a user interface
