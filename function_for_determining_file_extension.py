import requests
import os
import argparse
from urllib.parse import urlparse


def get_file_extension(url):
    url_parts = urlparse(url)
    path_with_file_extension = url_parts.path
    path, file_extension = os.path.splitext(path_with_file_extension)
    return file_extension


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Программа печатает расширение файла"
    )
    parser.add_argument("url", help="Ссылка, содержащая расширение файла")
    args = parser.parse_args()
    print(get_file_extension(args.url))
