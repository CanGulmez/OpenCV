import numpy as np 
import cv2

# Read photos

path = "C:/Users/90545/DATA SCIENCE/07 - OpenCV/00 - Resources/01 - Photos/Dog1.jpg"

img = cv2.imread(path)

cv2.imshow("img", img)

cv2.waitKey(0)


# Read videos

path = "C:/Users/90545/DATA SCIENCE/07 - OpenCV/00 - Resources/02 - Videos/Animals.mp4"

capture = cv2.VideoCapture(path)

while True:

    isTrue, frame = capture.read()
    cv2.imshow("Animals", frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()

# Open Webcam

capture = cv2.VideoCapture(0)

while True:

    isTrue, frame = capture.read()
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()