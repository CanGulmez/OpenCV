import numpy as np 
import cv2

path = "C:/Users/90545/DATA SCIENCE/07 - OpenCV/00 - Resources/01 - Photos/Dog1.jpg"

img = cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (9, 9), 1)
imgCanny = cv2.Canny(img, 70, 70)

kernel = np.ones((5, 5), np.uint8)

imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


cv2.imshow("img", img)
# cv2.imshow("imgGray", imgGray)
# cv2.imshow("imgBlur", imgBlur)
# cv2.imshow("imgCanny", imgCanny)
# cv2.imshow("imgDialation", imgDialation)
# cv2.imshow("imgEroded", imgEroded)

cv2.waitKey(0)