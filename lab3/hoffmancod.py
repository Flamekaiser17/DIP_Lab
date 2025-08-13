import cv2
import numpy as np
from collections import Counter
import heapq
import matplotlib.pyplot as plt

# =================================
# Node structure for Huffman Tree
# =================================
class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol  # Pixel value (0–255) or None for internal nodes
        self.freq = freq      # Frequency of the symbol
        self.left = None
        self.right = None

    # Define comparison for heapq (based on frequency)
    def __lt__(self, other):
        return self.freq < other.freq


# =================================
# Build Huffman Tree
# =================================
def build_huffman_tree(frequency):
    # Create leaf nodes for each symbol and push into min-heap
    heap = [Node(sym, freq) for sym, freq in frequency.items()]
    heapq.heapify(heap)

    # Merge nodes until only one root node remains
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # Root of the Huffman Tree


# =================================
# Generate Huffman Codes
# =================================
def generate_codes(node, code="", codes=None):
    if codes is None:
        codes = {}
    if node is None:
        return
    if node.symbol is not None:
        codes[node.symbol] = code  # Assign code to symbol
        return
    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)
    return codes


# =================================
# Huffman Encode
# =================================
def huffman_encode(data):
    frequency = Counter(data)                  # Count pixel frequencies
    root = build_huffman_tree(frequency)       # Build tree
    codes = generate_codes(root)               # Generate codes
    encoded_data = ''.join(codes[pixel] for pixel in data)  # Encode all pixels
    return encoded_data, codes


# =================================
# Huffman Decode
# =================================
def huffman_decode(encoded_data, codes):
    reverse_codes = {v: k for k, v in codes.items()}  # Reverse map
    decoded_pixels = []
    current_code = ""
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_pixels.append(reverse_codes[current_code])
            current_code = ""
    return decoded_pixels


# =================================
# Main Processing
# =================================
# 1. Load grayscale image
img = cv2.imread(r"D:\Dip\download.jpeg", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("Image not found. Check the file path.")

# Flatten image into 1D list for processing
pixels = img.flatten().tolist()

# 2. Huffman Encoding
encoded_data, codes = huffman_encode(pixels)
print("Huffman Codes:", codes)
print(f"Original Size (bits): {len(pixels) * 8}")
print(f"Compressed Size (bits): {len(encoded_data)}")
print(f"Compression Ratio: {(len(pixels) * 8) / len(encoded_data):.2f}")

# 3. Huffman Decoding (Reconstruction)
decoded_pixels = huffman_decode(encoded_data, codes)
decoded_img = np.array(decoded_pixels, dtype=np.uint8).reshape(img.shape)

# 4. Display results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Decoded Image (After Huffman)")
plt.imshow(decoded_img, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
