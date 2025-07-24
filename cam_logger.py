import cv2
import time
from datetime import datetime
import os

cap = cv2.VideoCapture(0)
os.makedirs("logs", exist_ok=True) # create logs folder

try:
    while cap.isOpened(): # while the cam is open
        ret, frame = cap.read()
        if ret: # if camera capture works
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"logs/{timestamp}.jpg"
            cv2.imwrite(filename, frame) # save image
            time.sleep(10) # wait 10 seconds every save
except KeyboardInterrupt: # ctrl + c interrupt
    print("GhostTap cam_logger stopped.")
cap.release()