import cv2
import numpy as np
from skimage.measure import shannon_entropy
import matplotlib.pyplot as plt

# ===============================
# 1. Read and convert to grayscale
# ===============================
# r"" ensures Windows path is read correctly
# IMREAD_GRAYSCALE loads the image in 1 channel (0-255)
img = cv2.imread(r"D:\Dip\download.jpeg", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("Image not found. Check the file path.")

# ===============================
# 2. Calculate Shannon Entropy
# ===============================
# Entropy measures the randomness or information content in an image
entropy_value = shannon_entropy(img)
print(f"Shannon Entropy: {entropy_value:.4f}")

# ===============================
# 3. Entropy-based transformation (Original Method)
# ===============================
# Scale pixel values by entropy (not a standard DIP method, just for demonstration)
entropy_scaled_img = ((img / 255.0) * entropy_value * 255)
entropy_scaled_img = np.clip(entropy_scaled_img, 0, 255).astype(np.uint8)

# ===============================
# 4. Entropy-based contrast enhancement
# ===============================
# Entropy max for 8-bit grayscale is around 8, so normalize by dividing by 8
scale_factor = entropy_value / 8.0
# alpha -> contrast factor, beta -> brightness shift
enhanced_img = cv2.convertScaleAbs(img, alpha=scale_factor, beta=0)

# ===============================
# 5. Display the results
# ===============================
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

# Entropy-Scaled Image
plt.subplot(1, 3, 2)
plt.title("Entropy Scaled")
plt.imshow(entropy_scaled_img, cmap='gray')
plt.axis('off')

# Contrast Enhanced Image
plt.subplot(1, 3, 3)
plt.title("Contrast Enhanced")
plt.imshow(enhanced_img, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
