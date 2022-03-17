from cv2 import cv2
import numpy as np

def back(*args):
    pass

def nothing(x):
    # any operation
    pass

# kamera
cap = cv2.VideoCapture(0)

# menu
cv2.namedWindow("Menu")
cv2.resizeWindow("Menu", 200, 150)
cv2.createTrackbar("green", "Menu", 0, 1, nothing)
cv2.createTrackbar("blue", "Menu", 0, 1, nothing)
cv2.createTrackbar("red", "Menu", 0, 1, nothing)

# font na text
font = cv2.FONT_HERSHEY_DUPLEX

while True:

    # okno s vypisom
    count = 255 * np.ones(shape=[600, 512, 3], dtype=np.uint8)

    # resetovanie pocitadiel
    red_count = 0
    blue_count = 0
    green_count = 0
    rect_count = 0
    circ_cout = 0
    triangle_count = 0

    # nacitanie hodnoty z trackbarov (posuvniky)
    green = cv2.getTrackbarPos("green", "Menu")
    blue = cv2.getTrackbarPos("blue", "Menu")
    red = cv2.getTrackbarPos("red", "Menu")

    # ziskanie HSV "mapy"
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # nastavenie HSV pre konkretne farby
    lower_green = np.array([35, 50, 0])
    upper_green = np.array([89, 255, 255])
   
    lower_red = np.array([0, 100, 50])
    upper_red = np.array([18, 255, 255])

    lower_blue = np.array([90, 50, 0])
    upper_blue = np.array([135, 255, 255])

    kernel = np.ones((5, 5), np.uint8) 

    #RED MASK
    red_mask = cv2.inRange(hsv, lower_red, upper_red)    
    red_mask = cv2.erode(red_mask, kernel)
        # Contours detection
    red_contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    #GREEN MASK
    green_mask = cv2.inRange(hsv, lower_green, upper_green)    
    green_mask = cv2.erode(green_mask, kernel)
        # Contours detection
    green_contours, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #BLUE_MAS
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)    
    blue_mask = cv2.erode(blue_mask, kernel)
        # Contours detection
    blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Ak je zapnute vyhladavanie cervenej...
    if(red==1):
        for cnt in red_contours:
            # pre kazdu konturu ziskame jej velkost
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            # ak je dost velka tak..
            if area > 400:
                # pricitame cerveny objekt a nakreslime kontury do kamery
                red_count = red_count + 1 
                cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
                if len(approx) == 3:
                    # ak ma tri steny tak je to trojuholnik...napiseme do kamery a pripocitam
                    cv2.putText(frame, "T", (x, y), font, 1.5, (0, 0, 255))
                    triangle_count = triangle_count + 1
                elif len(approx) == 4:
                    x,y,w,h=cv2.boundingRect(approx)
                    aspectRatio = float (w)/h
                    if aspectRatio >=0.95 and aspectRatio <=1.05:
                        cv2.putText(frame, "S", (x, y), font, 1.5, (0, 0, 255))
                        rect_count = rect_count + 1
                    else:
                        cv2.putText(frame, "R", (x, y), font, 1.5, (0, 0, 255))
                        rect_count = rect_count + 1
                elif 6 < len(approx) < 20:
                    cv2.putText(frame, "C", (x, y), font, 1.5, (0, 0, 255))
                    circ_cout = circ_cout + 1
                

    # to iste..
    if(green==1):
        for cnt in green_contours:
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            if area > 400:
                green_count = green_count +1
                cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
                if len(approx) == 3:
                    cv2.putText(frame, "T", (x, y), font, 1.5, (0, 255, 0))
                    triangle_count = triangle_count + 1
                elif len(approx) == 4:
                    x,y,w,h=cv2.boundingRect(approx)
                    aspectRatio = float (w)/h
                    if aspectRatio >=0.95 and aspectRatio <=1.05:
                        cv2.putText(frame, "S", (x, y), font, 1.5, (0, 255, 0))
                        rect_count = rect_count + 1
                    else:
                        cv2.putText(frame, "R", (x, y), font, 1.5, (0, 255, 0))
                        rect_count = rect_count + 1
                elif 6 < len(approx) < 20:
                    cv2.putText(frame, "C", (x, y), font, 1.5, (0, 255, 0))
                    circ_cout = circ_cout + 1
            

    if(blue==1):
        for cnt in blue_contours:
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            if area > 400:
                blue_count = blue_count + 1
                cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
                if len(approx) == 3:
                    cv2.putText(frame, "T", (x, y), font, 1.5, (255, 0, 0))
                    triangle_count = triangle_count + 1
                elif len(approx) == 4:
                    x,y,w,h=cv2.boundingRect(approx)
                    aspectRatio = float (w)/h
                    if aspectRatio >=0.95 and aspectRatio <=1.05:
                        cv2.putText(frame, "S", (x, y), font, 1.5, (255, 0, 0))
                        rect_count = rect_count + 1
                    else:
                        cv2.putText(frame, "R", (x, y), font, 1.5, (255, 0, 0))
                        rect_count = rect_count + 1
                elif 6 < len(approx) < 20:
                    cv2.putText(frame, "C", (x, y), font, 1.5, (255, 0, 0))
                    circ_cout = circ_cout + 1
            

    # vsetky obrazce
    all_count = red_count + blue_count + green_count
   
    # vypis
    cv2.putText(count, "Number of objects: "+str(all_count), (60, 90), font, 1, (0, 0, 0))
    cv2.putText(count, "Red objects: "+str(red_count), (60, 200), font, 1, (0, 0, 0))
    cv2.putText(count, "Blue objects: "+str(blue_count), (60, 250), font, 1, (0, 0, 0))
    cv2.putText(count, "Green objects: "+str(green_count), (60, 300), font, 1, (0, 0, 0))

    cv2.putText(count, "Num. of triangles: "+str(triangle_count), (60, 400), font, 1, (0, 0, 0))
    cv2.putText(count, "Num. of rectangle: "+str(rect_count), (60, 450), font, 1, (0, 0, 0))
    cv2.putText(count, "Num. of circles: "+str(circ_cout), (60, 500), font, 1, (0, 0, 0))

    # zobrazenie obrazovky (refresh)
    cv2.imshow("Frame", frame)
    cv2.imshow("Count", count)
    if red==1 and blue==0 and green==0:
        cv2.imshow("Mask",red_mask)
    elif red==0 and blue==1 and green==0:
        cv2.imshow("Mask",blue_mask)
    elif red==0 and blue==0 and green==1:
        cv2.imshow("Mask",green_mask)
    elif red==1 and blue==1 and green==0:
        cv2.imshow("Mask",red_mask+blue_mask)
    elif red==0 and blue==1 and green==1:
        cv2.imshow("Mask",green_mask+blue_mask)
    elif red==1 and blue==0 and green==1:
        cv2.imshow("Mask",green_mask+red_mask)
    elif red==1 and blue==1 and green==1:
        cv2.imshow("Mask",green_mask+red_mask+blue_mask)
        
        
        
        
    
    # ak stlacime ESC vypneme apku
    key = cv2.waitKey(1)
    if key == 27:
        break

# uvolnime kameru a zavrieme okna
cap.release()
cv2.destroyAllWindows()
