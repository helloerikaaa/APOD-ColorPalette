import extcolors
import pandas as pd
from loguru import logger
from colormap import rgb2hex


class ColorExtractor:
    def __init__(self, img):
        self.img = img

    def _extract_colors(self):
        logger.info("Extracting colors from image")
        colors = extcolors.extract_from_image(self.img, tolerance=12, limit=12)
        return colors

    def _convert_rgb_to_hex(self, colors):
        logger.info("Converting rgb colors to hex")
        hex_colors = [
            rgb2hex(
                int(i.split(", ")[0].replace("(", "")),
                int(i.split(", ")[1]),
                int(i.split(", ")[2].replace(")", "")),
            )
            for i in colors
        ]
        return hex_colors

    def get_color_list(self):
        colors = list(self._get_image_colors()["hex_code"])
        logger.info("Extracted colors in hex successfully")
        return colors

    def _get_image_colors(self):
        logger.info("Saving image colors to DataFrame")
        colors = self._extract_colors()

        colors_pre_list = str(colors).replace("([(", "").split(", (")[0:-1]
        rgb_colors = [i.split("), ")[0] + ")" for i in colors_pre_list]
        percent = [i.split("), ")[1].replace(")", "") for i in colors_pre_list]
        hex_colors = self._convert_rgb_to_hex(rgb_colors)

        data = pd.DataFrame(zip(hex_colors, percent), columns=["hex_code", "occurence"])

        return data
