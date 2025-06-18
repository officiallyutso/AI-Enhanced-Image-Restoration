import os
import warnings
from PIL import Image

def suppress_warnings():
    """Suppress common warnings."""
    warnings.filterwarnings("ignore", category=UserWarning)
    
def validate_image_path(image_path):
    """Validate if image path exists and is valid."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    _, ext = os.path.splitext(image_path.lower())
    if ext not in valid_extensions:
        raise ValueError(f"Unsupported image format: {ext}")