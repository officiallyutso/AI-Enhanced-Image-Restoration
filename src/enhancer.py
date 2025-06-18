import cv2
import torch
from gfpgan.utils import GFPGANer
from realesrgan.utils import RealESRGANer
from basicsr.archs.srvgg_arch import SRVGGNetCompact
from .config import *


class ImageEnhancer:
    """Main image enhancement class."""
    
    def __init__(self):
        self.sr_model = None
        self.face_enhancer = None
        self._load_models()
        
    