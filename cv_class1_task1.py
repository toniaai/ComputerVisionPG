#16-04-2019 antonio aguirre ivorra
import cv2
from matplotlib import pyplot as plt


def task1_mycode(image1, image2, windowTitle):
    fig = plt.figure(windowTitle)

    #first image:
    imagen_ax = fig.add_subplot(1,2,1)
    plt.imshow(image1)
    plt.axis("off")

    #second image:
    imagen_ax = fig.add_subplot(1,2,2)
    plt.imshow(image2)
    plt.axis("off")

    plt.show()


def task1_given(img):
    # "Imagen" stands for image, name of our window
    cv2.imshow('Imagen', img)

    k = cv2.waitKey(0)

    if k == 27:
        cv2.destroyAllWindows()

#task 1: file reading
img = cv2.imread('images/test.png')

# we create a new image with the BGR transformation this way
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


task1_mycode(img, img2, "Comparison")

