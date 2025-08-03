Digital Image Processing Laboratory (Python)

This repository contains lab experiments and assignments for the Digital Image Processing (DIP) course, implemented in Python using OpenCV as part of the academic curriculum.

📁 Folder Structure

Each experiment is placed in a separate Python file, and input/output images are stored in a structured directory format.

DIP_Lab/
│
├── images/
│   └── download.jpeg             # Input image
│
├── output/
│   ├── output_gray.jpg           # Grayscale result
│   ├── output_blue_only.jpg      # Blue plane only
│   └── output_bw.jpg             # Binary (B&W) image
│
├── exp1_rgb_processing.py        # Python file for Experiment 1
└── README.md                     # This file


Experiment 1: RGB to Grayscale, RGB Planes, Black & White

# Objective

# To process a color image using the following techniques:

1.Convert RGB image to Grayscale.

2.Extract and display individual Red, Green, and Blue color planes.

3.Convert RGB image to Black and White (Binary) using thresholding.


 Output

All output images will be saved in the output/ folder:

output_gray.jpg → Grayscale conversion.

output_blue_only.jpg → Blue plane extracted (Red & Green removed).

output_bw.jpg → Black & White (Binary) image.

