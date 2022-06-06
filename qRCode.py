import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

imageSource = cv.imread('venv/lib/images/2.png')
imageSource = cv.resize(imageSource, (0, 0), fx=0.3, fy=0.3)
imageSource = cv.cvtColor(imageSource, cv.IMREAD_COLOR)

templateImage = cv.imread('venv/lib/templats_images/1.png')
templateImage = cv.resize(templateImage, (0, 0), fx=0.3, fy=0.3)
templateImage = cv.cvtColor(templateImage, cv.IMREAD_COLOR)

w, h = templateImage.shape[:-1]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    newImageSource = imageSource.copy()
    method = eval(meth)
    # Apply template Matching
    result = cv.matchTemplate(newImageSource, templateImage,  method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(newImageSource, top_left, bottom_right, 255, 1)

    plt.plot()
    plt.imshow(newImageSource)
    plt.title('Detected Point')

    plt.xticks([])
    plt.yticks([])

    plt.suptitle(meth)
    plt.show()
