import tensorflow as tf
import numpy as np
import cv2
import os

# Load the model
model = tf.keras.models.load_model('model/')

# Class names
class_names = ['Daenerys', 'Jon Snow']

# Folder with test images
test_folder = 'test_images'

# Test images in the folder
for img_name in os.listdir(test_folder):
    img_path = os.path.join(test_folder, img_name)
    img = cv2.imread(img_path)
    if img is None:
        print(f'Could not read image: {img_name}')
        continue

    img_resized = cv2.resize(img, (224, 224))
    img_array = np.expand_dims(img_resized / 255.0, axis=0)

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]

    print(f'Image: {img_name} → Prediction: {predicted_class}')
