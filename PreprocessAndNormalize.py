import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import os

def preprocess_images(full_image_path, target_size=(512, 212)):
     # Read the image using OpenCV
    image = cv2.imread(full_image_path)

    # Convert BGR to RGB (OpenCV uses BGR by default)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize the image to the target size
    image = cv2.resize(image, (512, 512))

    image = cv2.GaussianBlur(image, (5, 5), 0)

    # Normalize pixel values to be in the range [0, 1]
    image = image / 255.0
    return image


def preprocess_and_normalize_images(image_folder, target_size=(512, 512)):
    normalized_images = []
    count = 0