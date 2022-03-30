import cv2
import numpy as np

imageSource = cv2.imread('venv/lib/images/4es.png')
imageSource = cv2.resize(imageSource, (0, 0), fx=0.4, fy=0.4)
imageSource = cv2.cvtColor(imageSource, cv2.IMREAD_COLOR)

templateImage = cv2.imread('venv/lib/images/A.png')
templateImage = cv2.resize(templateImage, (0, 0), fx=0.7, fy=0.8)
templateImage = cv2.cvtColor(templateImage, cv2.IMREAD_COLOR)


height, width = templateImage.shape[:-1]

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED]

for method in methods:
    newImageSource = imageSource.copy()

    result = cv2.matchTemplate(newImageSource, templateImage, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [ cv2.TM_CCOEFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
        bottom_right = (location[0] + width, location[1] + height)
        cv2.rectangle(newImageSource, location, bottom_right, 255, 2)
        cv2.imshow('Match', newImageSource)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
