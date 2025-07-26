import requests
import os

def upload_file(file_path):
    url = "http://127.0.0.1:5000/upload" # server url
    
    try:
        with open(file_path, "rb") as f:
            files = {'file': f}
            response = requests.post(url, files=files)
            
        if response.status_code == 200:
            print(f"UPLOAD SUCCESSFUL: {file_path}")
            os.remove(file_path)
        else:
            print(f"[UPLOAD FAIL] {response.status_code}: {response.text}")
    except Exception as e:
        print(f"[UPLOAD ERROR] {e}")
