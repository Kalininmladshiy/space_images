import requests
import argparse
from pathlib import Path


def download_pictures(
    path_to_pictures,
    filename,
    url="https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
     ):
    response = requests.get(url)
    response.raise_for_status()
    with open(Path() / path_to_pictures / filename, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Программа для скачивания картинок"
    )
    parser.add_argument("--url", help="Ссылка на картинку")
    args = parser.parse_args()
    filename = 'space.jpeg'
    path_to_pictures = Path.cwd() / 'images' 
    if args.url:
        try:
            download_pictures(path_to_pictures, filename, args.url)
        except requests.exceptions.HTTPError as e:
            print(e.response.status_code)
    else:
        try:
            download_pictures(path_to_pictures, filename)
        except requests.exceptions.HTTPError as e:
            print(e.response.status_code)
