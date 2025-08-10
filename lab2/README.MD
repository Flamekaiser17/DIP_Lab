
Experiment 2A – Histogram Equalization
📌 Description

Histogram equalization is a fundamental technique in image processing used to improve contrast. It works by spreading out the most frequent pixel intensity values, effectively stretching the image's dynamic range.

Think of a dark photo where everything is clumped together in the shadows. Histogram equalization takes those clumped values and redistributes them across the entire intensity range (0–255), making hidden details visible. This is achieved by attempting to create a "flat" or uniform histogram.

🎯 Objectives

Understand the concept of an image histogram and its relation to image contrast.

Implement histogram equalization on a grayscale image using Python's OpenCV library.

Visually compare an image and its histogram before and after equalization to see the improvement.

⚙️ Logic (Python Implementation)

Read the input image in grayscale using cv2.imread('image.jpg', 0).

Apply histogram equalization using the built-in OpenCV function: equalized_img = cv2.equalizeHist(original_img).

Use Matplotlib to create a 2x2 plot for comparison:

Top-left: Display the original, low-contrast image.

Bottom-left: Display the histogram of the original image.

Top-right: Display the new, high-contrast equalized image.

Bottom-right: Display the uniform histogram of the equalized image.

🖼️ Sample Output

The output will clearly show the contrast enhancement. The equalized image will have more distinct details in both dark and bright areas. Its histogram will be spread out across the entire range, unlike the original histogram which may have been clustered in one area.

✍️ Author

Name: Shivansh

Roll No.: BT23ECI011

Experiment 2B – Bit Slicing in Digital Image Processing
📌 Description

This experiment demonstrates bit-plane slicing on a grayscale image using Python with libraries like OpenCV and Matplotlib. Bit slicing is a technique used to analyze specific bits of pixel intensity values, which helps in image compression, enhancement, and feature extraction.

Each pixel in a grayscale image is typically represented using 8 bits (values from 0 to 255). Bit slicing helps isolate individual bit-planes from these 8-bit representations.

🎯 Objectives

Understand and implement the concept of bit-plane slicing in Python.

Extract all 8 bit-planes from an image using efficient vectorized operations.

Display the contribution of each bit to the overall image quality.

⚙️ Logic (Python Implementation)

Read the input image in grayscale using cv2.imread().

Create an empty list to store the 8 bit-plane images.

Loop from bit 0 to 7:

For each bit i, create a mask which is a power of 2 (e.g., 2**i).

Apply a bitwise AND operation between the entire image array and the mask. This efficiently isolates the i-th bit for all pixels at once.

For visualization, normalize the resulting plane by converting its non-zero values to 255 (white).

Store the resulting binary image in the list of bit-planes.

Use Matplotlib to display the original image and each bit-plane in a subplot grid.

🖼️ Sample Output

Each bit-plane will be displayed as an 8-bit grayscale image.

Bit-plane 7 (MSB) shows the most significant details and resembles the original image.

Bit-plane 0 (LSB) shows the least significant details, which often appear as random noise.

✍️ Author

Name: Shivansh

Roll No.: BT23ECI011