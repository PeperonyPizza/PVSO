import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
kernel = np.ones((5, 5))
while (cap.isOpened()):
    ret, frame = cap.read()
    img = frame
    if ret == True:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(frame, 140, 255, cv2.THRESH_BINARY_INV) #korektne
        erode = cv2.erode(frame, kernel, )
        blur = cv2.GaussianBlur(erode, (3, 3), 0)
        _, thresh = cv2.threshold(blur, 160, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
       # _, thresh = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 12)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            if area > 8000:
                cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
                if len(approx) == 3:
                    print(approx)
                    cv2.putText(img, "Triangle", (x, y), 1, 1, (255, 0, 0), 2)
                elif len(approx) == 4:
                    print(approx)
                    cv2.putText(img, "Rectangle", (x, y), 1, 1, (255, 0, 0), 2)
                elif 10 < len(approx) < 15:
                    print(approx)
                    cv2.putText(img, "Circle", (x, y), 1, 1, (255, 0, 0), 2)

        cv2.imshow('blur', erode)
        cv2.imshow('thresh', thresh)
        cv2.imshow('result', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
