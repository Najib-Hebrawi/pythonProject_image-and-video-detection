import numpy as np
import cv2

"""""
load video.    0 for number of the webcam, in case that we have more than one webcam,
 we can also use a file after opleading that to our project
"""""
capture = cv2.VideoCapture(0)
"""""
while method, to keep the webcam working.
"""""
while True:
    ret, frame = capture.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
