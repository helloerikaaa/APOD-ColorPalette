import requests
import urllib.request

from PIL import Image
from loguru import logger

from consts.consts import API_URL
from consts.paths import APODPaths


def download_apod_image():
    r = requests.get(API_URL)
    path = APODPaths.image_path
    img = None

    if r.status_code == 200:
        results = r.json()
        url = results["hdurl"]
        logger.info(f"Fetching APOD image from {url}")

        if results["media_type"] == "image":
            urllib.request.urlretrieve(url, "apod.png")
            img = Image.open("apod.png")
            logger.info(f"Image retrieved successfully. Saved to {path}")
        else:
            logger.error("APOD of today is not an image")
    else:
        logger.error("Could not make the request to NASA. Please try again")
    return img
