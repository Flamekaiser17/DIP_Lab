# -----------------------------------------------------------
# DIGITAL IMAGE PROCESSING LAB
# Experiment 5: Edge Detection using Sobel, Prewitt, and Laplacian Operators
# -----------------------------------------------------------

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

# Step 1: Read the input image safely
img_path = r"D:\Dip\lab5\dog.jpg"

if not os.path.exists(img_path):
    print("❌ Error: File not found at", img_path)
    exit()

img = cv2.imread(img_path)

if img is None:
    print("❌ Error: Failed to load image. It might be corrupted or in an unsupported format.")
    exit()
else:
    print("✅ Image loaded successfully with shape:", img.shape)

# Step 2: Convert BGR to RGB for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img_rgb)
plt.title('Original Image')
plt.axis('off')

# Step 3: Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 4: Sobel Operator
sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = cv2.convertScaleAbs(cv2.magnitude(sobel_x, sobel_y))

# Step 5: Prewitt Operator (manual)
kernelx = np.array([[1, 0, -1],
                    [1, 0, -1],
                    [1, 0, -1]])
kernely = np.array([[1, 1, 1],
                    [0, 0, 0],
                    [-1, -1, -1]])
prewitt_x = cv2.filter2D(gray_img, -1, kernelx)
prewitt_y = cv2.filter2D(gray_img, -1, kernely)
prewitt_edges = cv2.add(prewitt_x, prewitt_y)

# Step 6: Laplacian Operator
laplacian_edges = cv2.convertScaleAbs(cv2.Laplacian(gray_img, cv2.CV_64F))

# Step 7: Display all
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1), plt.imshow(gray_img, cmap='gray'), plt.title('Grayscale Image'), plt.axis('off')
plt.subplot(2, 2, 2), plt.imshow(sobel_edges, cmap='gray'), plt.title('Sobel Operator'), plt.axis('off')
plt.subplot(2, 2, 3), plt.imshow(prewitt_edges, cmap='gray'), plt.title('Prewitt Operator'), plt.axis('off')
plt.subplot(2, 2, 4), plt.imshow(laplacian_edges, cmap='gray'), plt.title('Laplacian Operator'), plt.axis('off')
plt.tight_layout()
plt.show()
