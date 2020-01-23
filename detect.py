import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
     # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask =red_mask)
    mask = red_mask
    #print("ReD")
    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    mask = blue_mask
    #print("Blue")
    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    mask = green_maska
    #print("Green")
    #Showing reult
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    '''if(mask.all() == red_mask.all()):
        print('Red')
    elif(mask.all() == blue_mask.all()):
        print('Blue')
    elif(mask.all() == green_mask.all()):
        print('Green')
        break'''

    #cv2.imshow("Result", result)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    #Distroy all HighGUI windows
cv2.destroyAllWindows()
    #release the captured frame
cap.release()

    
