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
        
    def _load_models(self):
        """Load RealESRGAN and GFPGAN models."""
        # Load RealESRGAN
        sr_model = SRVGGNetCompact(
            num_in_ch=3, num_out_ch=3, num_feat=64, 
            num_conv=32, upscale=4, act_type='prelu'
        )
        half = True if torch.cuda.is_available() else False
        
        self.sr_model = RealESRGANer(
            scale=REALESRGAN_SCALE,
            model_path=REALESRGAN_MODEL_PATH,
            model=sr_model,
            tile=REALESRGAN_TILE,
            tile_pad=REALESRGAN_TILE_PAD,
            pre_pad=REALESRGAN_PRE_PAD,
            half=half
        )
        
        # Load GFPGAN
        self.face_enhancer = GFPGANer(
            model_path=GFPGAN_MODEL_PATH,
            upscale=GFPGAN_UPSCALE,
            arch=GFPGAN_ARCH,
            channel_multiplier=GFPGAN_CHANNEL_MULTIPLIER,
            bg_upsampler=self.sr_model
        )
        
    def upscale_image(self, image_path, output_path):
        """Upscale image using RealESRGAN."""
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        output, _ = self.sr_model.enhance(img, outscale=4)
        cv2.imwrite(output_path, output)
        return output
    
    def enhance_faces(self, image_path, output_path):
        """Enhance faces in image using GFPGAN."""
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        _, _, img_enhanced = self.face_enhancer.enhance(
            img, has_aligned=False, only_center_face=False, paste_back=True
        )
        cv2.imwrite(output_path, img_enhanced)
        return img_enhanced