import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv
from function_for_determining_file_extension import get_file_extension
from function_for_download_pictures import download_pictures


def fetch_nasa_launch(url, payload, path_to_pictures):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for photo_number, day_nasa_photo in enumerate(response.json()):
        download_pictures(
            day_nasa_photo['url'],
            path_to_pictures,
            f'nasa_{photo_number}{get_file_extension(day_nasa_photo["url"])}',
        )


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']    
    path_to_pictures = './images/'
    nasa_payload = {
        'api_key': nasa_api_key,
        'count': 10
    }
    parser = argparse.ArgumentParser(
        description='Программа для загрузки изображений NASA'
    )
    parser.add_argument("url", help="Ссылка для скачивания изображений")
    args = parser.parse_args()
    try:
        fetch_nasa_launch(
            args.url,
            nasa_payload,
            path_to_pictures
        )
    except requests.exceptions.HTTPError as e:
        print(e.response.status_code)
