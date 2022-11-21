import requests
from loguru import logger

from consts.consts import API_URL

def download_apod_image(path):
    r = requests.get(API_URL)
    
    if r.status_code == 200:
        results = r.json()
        url = results['hdurl']
        logger.info(f'Fetching APOD image from {url}')
        
        if results['media_type'] == 'image':
            with open(path, 'wb') as f:
                f.write(requests.get(url).content)
            logger.info(f'Image retrieved successfully. Saved to {path}')
        else:
            logger.error('APOD of today is not an image')
    else:
        logger.error('Could not make the request to NASA. Please try again')
