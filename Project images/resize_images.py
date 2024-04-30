import cv2
import os

# Function to resize images
def resize_images(input_dir, output_dir, target_size):
    # Create output directory if not exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through each file in the input directory
    for filename in os.listdir(input_dir):
        # Read the image
        img = cv2.imread(os.path.join(input_dir, filename))
        if img is not None:
            # Resize the image
            resized_img = cv2.resize(img, target_size)
            # Save the resized image
            cv2.imwrite(os.path.join(output_dir, filename), resized_img)
            print(f"Resized: {filename}")
        else:
            print(f"Could not read: {filename}")

# Input and output directories
input_dir = "./natural_images/person"
output_dir = "./resized/person"

# Target size for resizing
target_size = (256, 256)  # Set your desired width and height

# Resize images
resize_images(input_dir, output_dir, target_size)
