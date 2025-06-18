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


def create_output_dir(output_path):
    """Create output directory if it doesn't exist."""
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

def resize_for_display(image_path, max_size=(800, 800)):
    """Resize image for display purposes."""
    image = Image.open(image_path)
    image.thumbnail(max_size, Image.LANCZOS)
    return image


def get_output_filename(input_path, suffix="_enhanced"):
    """Generate output filename based on input path."""
    dir_path = os.path.dirname(input_path)
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    ext = os.path.splitext(input_path)[1]
    return os.path.join(dir_path, f"{base_name}{suffix}{ext}")