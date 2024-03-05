import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import os

def preprocess_images(full_image_path, target_size=(512, 212)):
     # Read the image using OpenCV
    image = cv2.imread(full_image_path)

    # Convert BGR to RGB (OpenCV uses BGR by default)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)