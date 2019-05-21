import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def harris(img):
    blockSize = 2
    apertureSize = 3
    k = 0.04
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, blockSize, apertureSize, k)
    dst = cv.dilate(dst, None)

    img[dst>0.01*dst.max()] = [0,0,255]

    cv.imshow('Harris', img)
    if cv.waitKey(0) & 0xFF == 27:
        cv.destroyAllWindows()

def harris_dif(img):
    thresh = 130
    blockSize = 2
    apertureSize = 3
    k = 0.04

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    dst = cv.cornerHarris(gray, blockSize, apertureSize, k)

    dst_normalized = np.empty(dst.shape, dtype=np.float32)
    cv.normalize(dst, dst_normalized, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
    dst_normalized_scaled = cv.convertScaleAbs(dst_normalized)

    for i in range(dst_normalized.shape[0]):
        for j in range(dst_normalized.shape[1]):
            if int(dst_normalized[i,j]) > thresh:
                cv.circle(img, (j,i), 5, (0), 2)

    cv.imshow('test', img)
    if cv.waitKey(0) & 0xFF == 27:
        cv.destroyAllWindwos()

def goodFeatures(img):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    edge = cv.goodFeaturesToTrack(gray, 20, 0.01, 10)
    edge = np.int0(edge)
    img2 = cv.imread('images/negro.jpg')
    for i in edge:
        x, y = i.ravel()
        cv.circle(img, (x,y), 3, 255, -1)
        #crop_img = img[y-20:y+20, x-20:x+20]
        #cv.add(img2, crop_img)
                                                                    
    plt.imshow(img),plt.show()

img = cv.imread('images/lena.png')
goodFeatures(img)
