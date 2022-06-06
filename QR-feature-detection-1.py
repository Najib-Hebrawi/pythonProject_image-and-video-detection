import cv2
import numpy as np
import os

img1 = cv2.imread("venv/lib/templats_images/1QRCardsAlone.png", 0)
img2 = cv2.imread("venv/lib/templats_images/1QRCardsAlone.png", 0)

# initialize our detector.
# orb is an algorithm that fri to use and fast.
orb = cv2.ORB_create(nfeatures=1000)

# now we will find our key points which are our features and the descriptors for images ( kp= key , des= description )
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# draw the key points on the picture
# imgkp1 = cv2.drawKeypoints(img1, kp1, None)


# our brute force matcher
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])

        print(len(good))
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

cv2.imshow("img1", img1)
# cv2.imshow("kp1", imgkp1)
cv2.imshow("img3", img3)
cv2.waitKey(0)
