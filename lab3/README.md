Experiment 3A – Shannon Entropy Based Image Processing

📌 Description:
----------------
Shannon entropy is a statistical measure of randomness that describes the amount of information in an image.

High entropy → more details, textures, or noise.

Low entropy → uniform or repetitive pixel values.

In this experiment, we:
----------------------
Calculate the Shannon entropy of a grayscale image.

Apply an entropy-based scaling transformation.

Enhance image contrast using entropy as a scaling factor.

🎯 Objectives:
--------------
To understand the concept of Shannon entropy in images.

To calculate entropy for a grayscale image.

To perform entropy-based image transformation and contrast enhancement.

To compare original and processed images.

⚙️ Logic:
---------
Read the input image in grayscale.

Calculate Shannon entropy using shannon_entropy() from skimage.measure.

Apply scaling transformation based on entropy value.

Enhance contrast using normalized entropy factor.

Display original, entropy-scaled, and contrast-enhanced images.

🖼️ Sample Output:
-----------------
Shannon Entropy: 7.4676

Original Image → Original grayscale version.

Entropy Scaled Image → Intensities scaled proportionally to entropy.

Contrast Enhanced Image → Contrast improved based on entropy.

✍️ Author:
Name: Shivansh
Roll No.: BT23ECI011


----------------------------------------------------------------------------------------------------------------------------


Experiment 3B – Huffman Coding for Image Compression

📌 Description:
---------------
Huffman coding is a lossless compression technique that assigns shorter codes to frequent pixel values and longer codes to less frequent ones, reducing storage without losing information.

In this experiment, we:

Calculate pixel frequencies in the image.

Build a Huffman tree and generate binary codes.

Encode the image into a compressed bitstream.

Decode the bitstream back into the original image.

🎯 Objectives:
--------------
To understand Huffman coding for lossless compression.

To implement Huffman encoding and decoding in Python.

To compute compression ratio.

To verify that the decoded image matches the original.

⚙️ Logic:
----------
Read the image in grayscale.

Flatten it into a list of pixel values.

Count frequency of each pixel using Counter().

Build Huffman tree using heapq.

Generate Huffman codes for each pixel value.

Encode all pixels into a binary string.

Decode binary string back to pixels.

Reshape to original image size and display results.

🖼️ Sample Output:
------------------
Huffman Codes: {34: '000000000', 217: '000000001', 190: '00000001', ... , 153: '1111111'} (truncated for brevity)

Original Size (bits): 405000

Compressed Size (bits): 379369

Compression Ratio: 1.07

Original Image and Decoded Image → Identical.

✍️ Author:
Name: Shivansh
Roll No.: BT23ECI011