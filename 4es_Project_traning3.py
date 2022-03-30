import cv2 as cv
import numpy as np

imageSource = cv.imread('venv/lib/images/4es.png', cv.IMREAD_UNCHANGED)
imageTemplate = cv.imread('venv/lib/templats_images/hjrte.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(imageSource, imageTemplate, cv.TM_CCOEFF_NORMED)

# get the best match position
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('best match confidence: %s' % max_val)


threshold = 0.8
if max_val >= threshold:
    print('found card')

    # get dimensions of the needle image
    card_width = imageTemplate.shape[1]
    card_height = imageTemplate.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + card_width, top_left[1] + card_height)

    cv.rectangle(imageSource, top_left, bottom_right,
                 color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    cv.imshow('Result', imageSource)
    cv.waitKey()

else:
    print('card not found')
