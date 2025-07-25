import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import os
import time

def mic_logger():
    os.makedirs("logs", exist_ok=True)
    duration = 8
    sample_rate = 44100

    try:
        while True:
            recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
            sd.wait()
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"logs/{timestamp}.wav"
            write(filename, sample_rate, recording)
            time.sleep(10)
    except KeyboardInterrupt:
        print("Mic logger stopped.")