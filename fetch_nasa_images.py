import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def download_pictures(url, path_to_pictures, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(f"{path_to_pictures}{filename}", 'wb') as file:
        file.write(response.content)


def fetch_nasa_launch(url, payload, path_to_pictures):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for photo_number, day_nasa_photo in enumerate(response.json()):
        download_pictures(
            day_nasa_photo['url'],
            path_to_pictures,
            f'nasa_{photo_number}{get_file_extension(day_nasa_photo["url"])}',
        )


def get_file_extension(url):
    url_parts = urlparse(url)
    path_with_file_extension = url_parts.path
    path, file_extension = os.path.splitext(path_with_file_extension)
    return file_extension


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
