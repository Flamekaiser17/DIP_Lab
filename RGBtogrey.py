import cv2

image = cv2.imread(r'D:\Dip\download.jpeg')

if image is None:
    print(" Failed to load image.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.imwrite(r'D:\Dip\output_gray.jpg', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
