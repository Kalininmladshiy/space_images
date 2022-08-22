import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv
from utils import get_file_extension
from utils import download_pictures
from pathlib import Path


def fetch_nasa_launch(
    path_to_pictures,
    payload,
    url='https://api.nasa.gov/planetary/apod',
     ):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for photo_number, day_nasa_photo in enumerate(response.json()):
        try:
            download_pictures(
                path_to_pictures,
                f'nasa_{photo_number}{get_file_extension(day_nasa_photo["url"])}',
                day_nasa_photo['url'],
            )
        except requests.exceptions.MissingSchema:
            continue


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    path_to_pictures = Path.cwd() / 'images'
    Path(path_to_pictures).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Программа для загрузки изображений NASA'
    )
    parser.add_argument("num", type=int,
                        help="Количество фотографий для скачивания")    
    parser.add_argument("--url", help="Ссылка для скачивания изображений")
    args = parser.parse_args()
    nasa_payload = {
        'api_key': nasa_api_key,
        'count': args.num
    }    
    if args.url:
        try:
            fetch_nasa_launch(
                path_to_pictures,
                nasa_payload,
                args.url,
            )
        except requests.exceptions.HTTPError as e:
            print(e.response.status_code)
    else:
        try:
            fetch_nasa_launch(
                path_to_pictures,
                nasa_payload,
            )
        except requests.exceptions.HTTPError as e:
            print(e.response.status_code)
