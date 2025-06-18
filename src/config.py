import os

# Model URLs
MODEL_URLS = {
    'realesr-general-x4v3.pth': "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-x4v3.pth",
    'GFPGANv1.4.pth': "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth",
}

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, 'models')
REALESRGAN_MODEL_PATH = os.path.join(MODELS_DIR, 'realesr-general-x4v3.pth')
GFPGAN_MODEL_PATH = os.path.join(MODELS_DIR, 'GFPGANv1.4.pth')

# Model parameters
REALESRGAN_SCALE = 4
REALESRGAN_TILE = 0
REALESRGAN_TILE_PAD = 10
REALESRGAN_PRE_PAD = 0

GFPGAN_UPSCALE = 10
GFPGAN_ARCH = 'clean'
GFPGAN_CHANNEL_MULTIPLIER = 2