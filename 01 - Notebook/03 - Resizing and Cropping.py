import numpy as np 
import cv2

path = "C:/Users/90545/DATA SCIENCE/07 - OpenCV/00 - Resources/01 - Photos/nature.jpg"

img = cv2.imread(path)

imgResize = cv2.resize(img, (640, 480))
imgCropped = img[0:100, 0:480]

# cv2.imshow("img", img)
# cv2.imshow("imgResize", imgResize)
# cv2.imshow("imgCropped", imgCropped)

cv2.waitKey(0)

print("img shape: {} \nimgResize shape: {} \nimgCropped shape: {}".format(img.shape, imgResize.shape, imgCropped.shape))