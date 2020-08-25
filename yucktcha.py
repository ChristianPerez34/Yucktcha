import os
from glob import glob

CAPTCHA_IMAGES_DIR = "images/captchas"
EXTRACTED_ALPHA_NUMERIC_DIR = "images/extracted_alpha_numeric"

class Yucktcha:
    def __init__(self):
        self.captcha_images = []

        if not os.path.exists(CAPTCHA_IMAGES_DIR):
            os.makedirs(CAPTCHA_IMAGES_DIR)

        if not os.path.exists(EXTRACTED_ALPHA_NUMERIC_DIR):
            os.makedirs(EXTRACTED_ALPHA_NUMERIC_DIR)

    def load_captchas(self):
        self.captcha_images = glob(f"{CAPTCHA_IMAGES_DIR}/*.png")
