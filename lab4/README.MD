# Experiment 4A – Arithmetic Image Transformations

📌 Description:
----------------
Arithmetic transformations are basic pixel-wise operations applied on digital images.
These operations modify brightness and contrast directly by applying addition, subtraction, multiplication, or division on pixel values.

In this experiment, we:
- Brighten an image using addition.
- Darken an image using subtraction.
- Increase contrast using multiplication.
- Decrease contrast using division.

🎯 Objectives:
--------------
- To understand arithmetic operations on images.
- To observe the effect of addition and subtraction on brightness.
- To observe the effect of multiplication and division on contrast.
- To compare original image with transformed images.

⚙️ Logic:
---------
1. Read the input image.
2. Convert it into RGB for proper display.
3. Perform arithmetic operations:
   - Addition (+) → Increases pixel values (brightening).
   - Subtraction (-) → Decreases pixel values (darkening).
   - Multiplication (×) → Increases contrast.
   - Division (÷) → Decreases contrast.
4. Display all images side by side for comparison.

🖼️ Sample Output:
-----------------
- Original Image
- Brightened Image (+50)
- Darkened Image (-50)
- Contrast Increased (×1.5)
- Contrast Decreased (÷1.5)

✍️ Author:
Name: Shivansh
Roll No.: BT23ECI011


------------------------------------------------------------


# Experiment 4B – JPEG Image Transformation

📌 Description:
----------------
JPEG is a commonly used lossy compression method for images.
By reducing quality, JPEG reduces storage requirements but introduces compression artifacts.

In this experiment, we:
- Encode an image into JPEG format with a given quality factor.
- Decode the compressed image back.
- Compare original image with JPEG compressed version.

🎯 Objectives:
--------------
- To understand JPEG image compression.
- To observe the effect of reduced quality on image clarity.
- To simulate JPEG compression using OpenCV.
- To visualize differences between original and compressed images.

⚙️ Logic:
---------
1. Read the input image.
2. Encode the image into JPEG format using cv2.imencode() with a lower quality (e.g., 30).
3. Decode it back using cv2.imdecode().
4. Display original vs compressed image.

🖼️ Sample Output:
-----------------
- Original Image
- JPEG Transformed Image (Quality = 30)

Visible artifacts (blurring, blockiness) appear in compressed image.

✍️ Author:
Name: Shivansh
Roll No.: BT23ECI011
