#16-04-2019 antonio aguirre ivorra
import numpy as np
import cv2 


# we will use again the code given in task 1 in order to show
# our image
def task1_given(img):
    # "Imagen" stands for image, name of our window
    cv2.imshow('Imagen', img)

    k = cv2.waitKey(0)

    if k == 27:
        cv2.destroyAllWindows()

def draw_stuff(img):
    # this will draw a rectangle with points (224, 202), (344, 384)
    # with the rgb colour of (0, 255, 0) and a thickness of 3 px
    cv2.rectangle(img,(224,202),(344,384),(0,255,0),3)

    # this will write the said text starting on the point (10,500)
    # using the font we defined in the variable font, white colour
    # (255, 255, 255) a thickness of 2 px and a lineType of cv2.LINE_AA
    # (line antialiasing)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'This is a signature', (10, 500), font, 1, (255,255,255), 2, cv2.LINE_AA)
    task1_given(img)


#task 3: file reading
img = cv2.imread('images/test.png')
draw_stuff(img)

