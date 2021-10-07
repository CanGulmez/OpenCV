import numpy as np 
import cv2

"""
(255, 0, 0) ==> blue color
(0, 255, 0) ==> green color
(0, 0, 250) ==> red color
(250, 0, 250) ==> pink color
(250, 250, 250) ==> white color
"""
img_1 = np.zeros((512, 512, 3), dtype=np.uint8)
img_1[:] = 255, 0, 0

img_2 = np.zeros((512,512, 3), dtype=np.uint8)
img_2[:400, :] = 0, 255, 0

"""
cv2.line(img, (a, b), (c, d), (color), (thickness))

a ==> start point and width
b ==> start point and height
c ==> last point and width
d ==> last point and height
"""
img_3 = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.line(img_3, (0, 0), (100, 100), (0, 250, 0), thickness=2)

img_4 = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.line(img_4, (10, 10), (200, 512), (0, 250, 0), thickness=2)

img_5 = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.line(img_5, (400, 30), (1, 100), (0, 250, 0), thickness=2)

"""
cv2.rectangle(img, (a, b), (c, d), (color), (thickness))
cv2.rectangle(img, (a, b), (c, d), (color), cv2.FILLED)

a ==> start point and width
b ==> start point and height
c ==> last point and width
d ==> last point and height
"""

img_6 = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.rectangle(img_6, (100, 100), (400, 400), (0, 250, 0), thickness=2)

img_7 = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.rectangle(img_7, (100, 100), (400, 400), (0, 250, 0), cv2.FILLED)

"""
cv2.circle(img, (a, b), c, (color), (thickness))
cv2.circle(img, (a, b), c, (color), cv2.FILLED)

a ==> start point and width
b ==> start point and height
c ==> radius
"""

img_8 = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.circle(img_8, (250, 250), 100, (0, 250, 0), thickness=2)

img_9 = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.circle(img_9, (250, 250), 100, (0, 250, 0), cv2.FILLED)

"""
cv2.putText(img, (text), (a, b), (font), (thickness), (color))

a ==> start point and width
b ==> start point and height
"""

img_10 = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.putText(img_10, "Hello World !!!", (150, 150), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 250, 0))

# cv2.imshow("img_1", img_1)
# cv2.imshow("img_2", img_2)
# cv2.imshow("img_3", img_3)
# cv2.imshow("img_4", img_4)
# cv2.imshow("img_5", img_5)
# cv2.imshow("img_6", img_6)
# cv2.imshow("img_7", img_7)
# cv2.imshow("img_8", img_8)
# cv2.imshow("img_9", img_9)
# cv2.imshow("img_10", img_10)


cv2.waitKey(0)