import os

from consts.consts import IMG_NAME

PROJECT_PATH = os.path.abspath(os.path.join(__file__, *(os.path.pardir,) * 3))
DATA_PATH = os.path.join(PROJECT_PATH, "data")
OUTPUT_PATH = os.path.join(DATA_PATH, "output")


class APODPaths:
    image_path = os.path.join(DATA_PATH, IMG_NAME)
