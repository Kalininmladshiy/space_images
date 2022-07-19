import requests
import argparse


def download_pictures(url, path_to_pictures, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(f"{path_to_pictures}{filename}", 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Программа для скачивания картинок"
    )
    parser.add_argument("url", help="Ссылка на картинку")
    args = parser.parse_args()
    filename = 'space.jpeg'
    path_to_pictures = './images/'
    filename = 'space.jpeg'
    try:
        download_pictures(args.url, path_to_pictures, filename)
    except requests.exceptions.HTTPError as e:
        print(e.response.status_code)
