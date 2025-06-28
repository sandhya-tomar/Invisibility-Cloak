from playsound import playsound
import cv2
import numpy as np
import time

# Start webcam
cap = cv2.VideoCapture(0)
time.sleep(2)
background = 0

# Capture background (you should stay out of frame for this)
for i in range(30):
    ret, background = cap.read()

background = np.flip(background, axis=1)

print("⚡ Mischief Managed! You’re now invisible like Harry Potter.")
playsound("cloak.wav")


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the color range for your cloak (adjust as needed)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask1 + mask2

    # Replace cloak with background
    mask_inv = cv2.bitwise_not(mask)
    res1 = cv2.bitwise_and(background, background, mask=mask)
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Harry Potter Invisibility Cloak", final_output)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
