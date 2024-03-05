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

    # Iterate over all files in the folder
    for filename in os.listdir(image_folder):
        count += 1
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Ensure the file is an image
            # Construct the full image path
            full_image_path = os.path.join(image_folder, filename)
            print("names: ", full_image_path)

            # Read and preprocess the image
            image = preprocess_images(full_image_path, target_size)

            # Append the normalized image to the list
            normalized_images.append(image)
            # normalized_images.append(full_image_path)

    return normalized_images


def plot_images(images, num_cols=3):
    num_images = len(images)
    num_rows = (num_images + num_cols - 1) // num_cols

    plt.figure(figsize=(15, 5 * num_rows))
    i = 0

    # for i in range(num_images):
    plt.subplot(num_rows, num_cols, i + 1)
    plt.imshow(images[i])
    plt.title(f"Image {i + 1}")
    plt.axis('off')

    plt.show()


image_folder = "/Users/eyosiasdesta/Desktop/GuardRails/Backend/Normalization/guardImages"
