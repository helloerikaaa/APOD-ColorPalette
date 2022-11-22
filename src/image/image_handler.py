from PIL import Image
from loguru import logger

from src.consts.paths import APODPaths
from src.consts.consts import RESIZE_WIDTH


class ImageHandler:
    def get_image(self, img_path):
        img = self._load_image(img_path)
        resized_img = self._resize_img(img)
        return resized_img

    def _load_image(self, img_path):
        logger.info("Loading image from disk")
        return Image.open(img_path)

    def _resize_img(self, img):
        logger.info("Resizing image")
        h, w = img.size
        w_percent = RESIZE_WIDTH / float(h)
        hsize = int((float(w) * float(w_percent)))
        resized_img = img.resize((RESIZE_WIDTH, hsize), Image.ANTIALIAS)
        resized_img.save(APODPaths.resized_img_path)
        logger.info(
            f"Image resized successfully. Saved to {APODPaths.resized_img_path}"
        )

        return resized_img
