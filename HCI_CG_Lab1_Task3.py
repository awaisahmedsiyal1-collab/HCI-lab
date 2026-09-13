# Task 3 — Channel Slicing & Isolation

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Make sure sample.jpg is in the same folder as this Python file
image = Image.open("sample.jpg").convert("RGB")
img = np.array(image)

# Extract RGB channels
red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

# Create 3D images with only one active channel
red_img = np.zeros_like(img)
green_img = np.zeros_like(img)
blue_img = np.zeros_like(img)

red_img[:, :, 0] = red
green_img[:, :, 1] = green
blue_img[:, :, 2] = blue

# Display original and isolated channels
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(red_img)
plt.title("Red Channel")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(green_img)
plt.title("Green Channel")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(blue_img)
plt.title("Blue Channel")
plt.axis("off")

plt.tight_layout()
plt.show()

print("Original Image Shape:", img.shape)
print("Red Channel 2D Shape:", red.shape)
print("Green Channel 2D Shape:", green.shape)
print("Blue Channel 2D Shape:", blue.shape)

print("Red Channel Mean Intensity:", round(red.mean(), 2))
print("Green Channel Mean Intensity:", round(green.mean(), 2))
print("Blue Channel Mean Intensity:", round(blue.mean(), 2))
