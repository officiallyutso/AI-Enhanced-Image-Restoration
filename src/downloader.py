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