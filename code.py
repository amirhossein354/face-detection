import cv2
import numpy as np

cap = cv2.VideoCapture("green-screen.mp4")
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        low = np.array([0, 40, 40])
        high = np.array([30, 255, 255])
        mask = cv2.inRange(frame, low, high)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
        cv2.imshow('mask', result)
        key = cv2.waitKey(1)
        if key != -1:
            print("video quited")
            break
    else:
        print("video finished")
        break
cv2.destroyAllWindows()
cap.release()
