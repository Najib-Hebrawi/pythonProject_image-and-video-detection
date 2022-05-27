import cv2

"""""
get the image from source
"""""
img = cv2.imread('venv/lib/images/4es.png', -1)
"""""
resize the image
"""""
img = cv2.resize(img, (500, 500))
"""""
rotate the image
"""""
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
"""""
show the image
"""""
cv2.imshow('image', img)
"""""
make a copy of image after manipulation
"""""
cv2.imwrite('venv/lib/images/mynewimageaftermunipulations.png', img)
"""""
wait to press any keys
"""""
cv2.waitKey(0)
"""""
change all windows too.
"""""
cv2.destroyAllWindows()
"""""
this talls me the number of rows(height),the numbers of columns(width), and the number of channels(just a color space of our image (how many pixels))
"""""
print(img.shape)
"""""
print images array (blue, green , red)
"""""
print(img)
"""""
print images first row of our image
"""""
print(img[0])
"""""
print images first row of our image, and the middle pixel(45:400)
"""""
print(img[0][45:400])
"""""
print images first row of our image, and the spicefic pixel(400)
"""""
print(img[0][400])
