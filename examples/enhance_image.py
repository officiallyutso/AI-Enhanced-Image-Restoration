import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.enhancer import ImageEnhancer
from src.downloader import download_models, verify_models
from src.utils import suppress_warnings, validate_image_path, create_output_dir


def main():
    """Main function to demonstrate image enhancement."""
    # Suppress warnings for cleaner output
    suppress_warnings()
    
    