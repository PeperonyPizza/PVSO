import cv2 
import numpy as np 
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
kernel = np.ones((5, 5))
while (cap.isOpened()):
    ret,frame=cap.read()
    img=frame
  if ret== True:
    # Convert to grayscale. 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
  
    # Blur using 3 * 3 kernel. 
    gray_blurred = cv2.blur(gray, (3, 3)) 
  
    # Apply Hough transform on the blurred image. 
    detected_circles = cv2.HoughCircles(gray_blurred,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
               param2 = 30, minRadius = 1, maxRadius = 40) 
  
    # Draw circles that are detected. 
    if detected_circles is not None: 
  
        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 
  
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
  
            # Draw the circumference of the circle. 
            cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
  
            # Draw a small circle (of radius 1) to show the center. 
            cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 
            cv2.imshow("Detected Circle", img) 
            cv2.waitKey(0)
   else:
        break
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
