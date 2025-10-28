📸 DIGITAL IMAGE PROCESSING LAB
This repository contains Python (OpenCV) codes, scripts, and resources for all Digital Image Processing (DIP) labs conducted during the course.

OBJECT DETECTION USING OPENCV

What is Object Detection?
Object detection is the process of identifying and locating objects within an image or video frame. It involves techniques such as feature extraction, edge detection, and contour analysis to detect and classify objects.

Objective:
In this lab, we demonstrate:

Loading an image using OpenCV

Converting color spaces (BGR → RGB)

Visualizing results using Matplotlib

TOOLS AND LIBRARIES USED

Python 3.10+

OpenCV (cv2)

NumPy

Matplotlib


CODE EXPLANATION
Step 1: Import Required Libraries

import cv2
import matplotlib.pyplot as plt
import os

Step 2: Load the Image

image_path = r"D:\Dip\lab5\dog.jpg"

if not os.path.exists(image_path):
print(f"❌ Error: Image not found at {image_path}")
exit()

img = cv2.imread(image_path)
if img is None:
print("❌ Error: Failed to load image. The file might be corrupted or unreadable.")
exit()

Step 3: Convert BGR to RGB and Display

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title("RGB Image - Object Detection Input")
plt.axis("off")
plt.show()

OUTPUT EXAMPLE

Stage: Original Image → Loaded using OpenCV
Stage: RGB Converted → After applying cv2.COLOR_BGR2RGB

(Replace with your actual images in the “output” folder if needed.)

REQUIREMENTS

Install dependencies using pip:
pip install opencv-python numpy matplotlib

If using a virtual environment:
python -m venv .venv
.venv\Scripts\activate
pip install opencv-python numpy matplotlib

COMMON ERRORS AND FIXES

Error: cv2.error: !_src.empty()
Reason: Image not found or corrupted
Fix: Check file path and image name

Error: NoneType from cv2.imread()
Reason: Invalid path or unreadable image
Fix: Use raw string path → r"D:\Dip\lab5\dog.jpg"

Error: matplotlib not found
Reason: Missing library
Fix: Run pip install matplotlib

NOTES

Always use absolute paths in Windows (r"D:\path\file.jpg").

Ensure the image file name matches exactly (case-sensitive).

You can modify the script to save processed images into an output folder.

REFERENCES

OpenCV Python Docs → https://docs.opencv.org/

Matplotlib Visualization → https://matplotlib.org/stable/

NumPy Documentation → https://numpy.org/doc/

AUTHOR

Bloody Ifang
Digital Image Processing Lab, IIIT Nagpur
Last Updated: October 2025