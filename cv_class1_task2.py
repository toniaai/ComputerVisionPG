#16-04-2019 antonio aguirre ivorra
import cv2 as cv2


cap = cv2.VideoCapture(0)



def show_video(cap):
    while(True):
        ret, frame = cap.read()

        # we apply the transformations now
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release() 
    cv2.destroyAllWindows() 

def save_video(cap):

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('images/video.avi', fourcc, 20.0, (640,480))

    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        out.write(frame)

        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()


save_video(cap)





