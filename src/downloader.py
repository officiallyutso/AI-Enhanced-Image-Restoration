import os
import requests
from .config import MODEL_URLS, MODELS_DIR


def download_file(url, filename):
    """Download file from URL with progress indication."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Downloaded {filename}")
        return True
    else:
        print(f"Failed to download {filename}. Status code: {response.status_code}")
        return False
    
def download_models():
    """Download all required model weights."""
    os.makedirs(MODELS_DIR, exist_ok=True)
    
    for filename, url in MODEL_URLS.items():
        file_path = os.path.join(MODELS_DIR, filename)
        if not os.path.exists(file_path):
            print(f"Downloading {filename}...")
            download_file(url, file_path)
        else:
            print(f"{filename} already exists. Skipping download.")


