import os
import warnings
from PIL import Image

def suppress_warnings():
    """Suppress common warnings."""
    warnings.filterwarnings("ignore", category=UserWarning)