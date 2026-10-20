
import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found")
        return

    colors = ('b', 'g', 'r')

    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=color.upper())

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Pixel Count")
    plt.legend()
    plt.show()

analyze_histogram("sample.jpg")
