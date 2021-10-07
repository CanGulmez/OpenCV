import numpy as np 
import cv2

path = "C:/Users/90545/DATA SCIENCE/07 - OpenCV/00 - Resources/01 - Photos/playing_card.jpg"

img = cv2.imread(path)

width, height = 320, 320

pts1 = np.float32([[30, 65], [330, 65], [30, 485], [330, 485]]) # left-top, right-top, left-bottom, right-bottom
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("img", img)
cv2.imshow("imgOutput", imgOutput)

cv2.waitKey(0)