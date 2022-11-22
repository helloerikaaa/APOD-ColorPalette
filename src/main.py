from loguru import logger

from src.consts.paths import APODPaths
from src.image.image_handler import ImageHandler
from src.api.api_handler import download_apod_image
from src.color.color_extractor import ColorExtractor


def main():
    logger.info("APOD Color Palette Generator")
    download_apod_image()

    image = ImageHandler().get_image(APODPaths.image_path)
    c_extractor = ColorExtractor(image)
    c_extractor.get_color_list()


if __name__ == "__main__":
    main()
