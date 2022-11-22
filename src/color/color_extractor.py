import extcolors
import pandas as pd
from loguru import logger
from colormap import rgb2hex
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches


from consts.paths import APODPaths, ColorPalettePaths


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

    def _create_background(self):
        fig, ax = plt.subplots(figsize=(160, 120), dpi=10)
        fig.set_facecolor("white")
        plt.savefig(ColorPalettePaths.output_path)
        plt.close(fig)

    def get_color_palette(self):
        logger.info("Creating color palette from image")
        self._create_background()

        img = mpimg.imread(APODPaths.resized_img_path)
        colors = list(self._get_image_colors()["hex_code"])
        background = plt.imread(ColorPalettePaths.output_path)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(160, 120), dpi=10)

        x_posi, y_posi, y_posi2 = 50, -100, -100
        for c in colors:
            if colors.index(c) <= 5:
                y_posi += 180
                rect = patches.Rectangle((x_posi, y_posi), 360, 160, facecolor=c)
                ax2.add_patch(rect)
                ax2.text(
                    x=x_posi + 400, y=y_posi + 100, s=c, fontdict={"fontsize": 190}
                )
            else:
                y_posi2 += 180
                rect = patches.Rectangle(
                    (x_posi + 1000, y_posi2), 360, 160, facecolor=c
                )
                ax2.add_artist(rect)
                ax2.text(
                    x=x_posi + 1400, y=y_posi2 + 100, s=c, fontdict={"fontsize": 190}
                )

        ax1.axis("off")
        ax2.axis("off")
        ax2.imshow(background)
        ax1.imshow(img)
        fig.set_facecolor("white")
        plt.savefig(ColorPalettePaths.output_path)
        logger.info(
            f"Color palette created successfully. Saved to {ColorPalettePaths.output_path}"
        )

    def _get_image_colors(self):
        logger.info("Saving image colors to DataFrame")
        colors = self._extract_colors()

        colors_pre_list = str(colors).replace("([(", "").split(", (")[0:-1]
        rgb_colors = [i.split("), ")[0] + ")" for i in colors_pre_list]
        percent = [i.split("), ")[1].replace(")", "") for i in colors_pre_list]
        hex_colors = self._convert_rgb_to_hex(rgb_colors)

        data = pd.DataFrame(zip(hex_colors, percent), columns=["hex_code", "occurence"])

        return data
