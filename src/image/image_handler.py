from PIL import Image
from loguru import logger

from consts.consts import RESIZE_WIDTH


class ImageHandler:
    def handle_image(self, img):
        resized_img = self._resize_img(img)
        return resized_img

    def _resize_img(self, img):
        logger.info("Resizing image")
        h, w = img.size
        w_percent = RESIZE_WIDTH / float(h)
        hsize = int((float(w) * float(w_percent)))
        resized_img = img.resize((RESIZE_WIDTH, hsize), Image.ANTIALIAS)
        return resized_img
