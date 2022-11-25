from PIL import Image
from loguru import logger

from consts.consts import RESIZE_WIDTH


class ImageHandler:
    def resize_img(self, img):
        logger.info("Resizing image")
        h, w = img.size
        w_percent = RESIZE_WIDTH / float(h)
        hsize = int((float(w) * float(w_percent)))
        resized_img = img.resize((RESIZE_WIDTH, hsize), Image.ANTIALIAS)
        return resized_img
