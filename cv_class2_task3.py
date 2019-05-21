import cv2
import numpy as np
from matplotlib import pyplot as plt


def selectROI(img_rgb):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    r = cv2.selectROI(img_rgb)
    template = img_gray[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    cv2.imshow('resultado', img_rgb)
    cv2.waitKey(0)

img_rgb = cv2.imread('images/combo2.jpg')
selectROI(img_rgb)
