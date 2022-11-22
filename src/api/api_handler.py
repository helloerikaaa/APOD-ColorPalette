import requests
from loguru import logger

from consts.consts import API_URL
from consts.paths import APODPaths


def download_apod_image():
    r = requests.get(API_URL)
    path = APODPaths.image_path

    if r.status_code == 200:
        results = r.json()
        url = results["hdurl"]
        logger.info(f"Fetching APOD image from {url}")

        if results["media_type"] == "image":
            with open(path, "wb") as f:
                f.write(requests.get(url).content)
            logger.info(f"Image retrieved successfully. Saved to {path}")
        else:
            logger.error("APOD of today is not an image")
    else:
        logger.error("Could not make the request to NASA. Please try again")
