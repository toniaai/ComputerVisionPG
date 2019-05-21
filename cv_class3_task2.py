import numpy as np
import cv2 as cv

def meanShift(cap):
    # take first frame of the video
    ret,frame = cap.read()

    r = cv.selectROI(frame)
    roi = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    x = r[0]
    y = r[1]
    w = r[2]
    h = r[3]
    track_window = (x, y, w, h)

    # set up the ROI for tracking
    hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV)
    gray_roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
    roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
    cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)

    # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
    term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )

    while(1):
        ret, frame = cap.read()

        if ret == True:
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)

            # apply meanshift to get the new location
            ret, track_window = cv.meanShift(dst, track_window, term_crit)

            # Draw it on image
            x,y,w,h = track_window
            img2 = cv.rectangle(frame, (x,y), (x+w,y+h), 255,2)
            cv.imshow('meanShift',img2)

            k = cv.waitKey(30) & 0xff
            if k == 27:
                break
        else:
            break

def camShift(cap):

    ret,frame = cap.read()

    r = cv.selectROI(frame)
    roi = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    x = r[0]
    y = r[1]
    w = r[2]
    h = r[3]
    track_window = (x, y, w, h)

    hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV)
    gray_roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
    roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
    cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
    # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
    term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )
    while(1):
        ret, frame = cap.read()
        if ret == True:
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
            # apply camshift to get the new location
            ret, track_window = cv.CamShift(dst, track_window, term_crit)
            # Draw it on image
            pts = cv.boxPoints(ret)
            pts = np.int0(pts)
            img2 = cv.polylines(frame,[pts],True, 255,2)
            cv.imshow('camShift',img2)
            k = cv.waitKey(30) & 0xff
            if k == 27:
                break
        else:
            break


cap = cv.VideoCapture(0);
option = input('Enter M for meanShift or C for camShift: ')

if option == 'M':
    meanShift(cap)
elif option == 'C':
    camShift(cap)
else: 
    print('Wrong option')
