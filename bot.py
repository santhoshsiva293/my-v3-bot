import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('Camera',frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break