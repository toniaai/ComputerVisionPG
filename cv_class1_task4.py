#16-04-19 antonio aguirre ivorra
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt



def nothing(x):
    pass

def given():
    # Create a black image, a window
    img = np.zeros((300,512,3), np.uint8)
    cv.namedWindow('image')
    # create trackbars for color change
    cv.createTrackbar('R','image',0,255,nothing)
    cv.createTrackbar('G','image',0,255,nothing)
    cv.createTrackbar('B','image',0,255,nothing)
    while(1):
        cv.imshow('image',img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
        # get current positions of four trackbars
        r = cv.getTrackbarPos('R','image')
        g = cv.getTrackbarPos('G','image')
        b = cv.getTrackbarPos('B','image')
        img[:] = [b,g,r]
    cv.destroyAllWindows()

def apply_thresholds(img):
    
    # we apply our different thresholds
    ret, th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
    ret3, th3 = cv.threshold(img,0,255,cv.THRESH_OTSU)

    titles = ['Original', 'Binary threshold', 'Adaptive Gausian', 'Otsu']
    images = [img, th1, th2, th3]

    # for every image we've stored in the images vector we add them
    # to a subplot of a figured and add their respective title
    # so we are able to know which threshold has been appplied 
    # to each one of the images.
    for image in range(4):
        plt.subplot(2,2,image+1),plt.imshow(images[image], 'gray')
        plt.title(titles[image])
        plt.xticks([]), plt.yticks([])

        # saves each image being shown as testX.png being X the index
        # of the image being iterated in the for loop
        cv.imwrite('test' + str(image) + '.png', images[image])

    plt.show()

img = cv.imread('test.png', 0)
apply_thresholds(img)








