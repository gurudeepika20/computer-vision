
import cv2

image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found")
else:
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blur Image", blurred_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
