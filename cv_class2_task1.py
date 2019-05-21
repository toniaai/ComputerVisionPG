import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def canny(img):
    edge = cv.Canny(img, 100, 200)
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Original')
    plt.subplot(122),plt.imshow(edge, cmap = 'gray')
    plt.title('Canny')
    plt.show()

def canny_thresh(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(gray, 100, 120)
    edge_thresh = cv.Canny(gray, 120, 200)
    plt.subplot(221),plt.imshow(gray, cmap = 'gray')
    plt.title('Original')
    plt.subplot(222),plt.imshow(edge, cmap = 'gray')
    plt.title('Canny')
    plt.subplot(223),plt.imshow(edge_thresh, cmap = 'gray')
    plt.title('Canny higher threshold')
    plt.show()


img = cv.imread('lena.jpg')
canny_thresh(img)
