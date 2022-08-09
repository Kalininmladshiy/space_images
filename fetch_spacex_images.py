import requests
import os
import argparse
from urllib.parse import urlparse
from function_for_determining_file_extension import get_file_extension
from function_for_download_pictures import download_pictures


def fetch_spacex_launch(url, path_to_pictures, flight_id='latest'):
    response = requests.get(url + flight_id)
    response.raise_for_status()
    spacex_photos = response.json()['links']['flickr']['original']
    for photo_number, photo in enumerate(spacex_photos):
        download_pictures(
            path_to_pictures,
            f'spacex_{photo_number}{get_file_extension(photo)}',
            photo,
        )


if __name__ == '__main__':
    path_to_pictures = './images/'
    parser = argparse.ArgumentParser(
        description='Программа для скачивания фото SpaceX'
    )
    parser.add_argument("url", help="ссылка на фотографии запуска")
    parser.add_argument(
        "--flight_id",
        help="id полета, фотографии которого хотим скачать",
    )
    args = parser.parse_args()
    if args.flight_id:
        try:
            fetch_spacex_launch(
                args.url,
                path_to_pictures,
                args.flight_id
            )
        except requests.exceptions.HTTPError as e:
            print(e.response.status_code)
    else:
        try:
            fetch_spacex_launch(
                args.url,
                path_to_pictures,
            )
        except requests.exceptions.HTTPError as e:
            print(e.response.status_code)
