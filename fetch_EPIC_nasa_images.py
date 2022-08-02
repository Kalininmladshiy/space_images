import requests
import os
import datetime
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv
from function_for_determining_file_extension import get_file_extension
from function_for_download_pictures import download_pictures


def fetch_epic_nasa_launch(
    payload,
    count_photo,
    path_to_pictures,
    epic_nasa_url='https://api.nasa.gov/EPIC/api/natural/images',
     ):
    response = requests.get(epic_nasa_url, params=payload)
    response.raise_for_status()
    for epic_photo_number, epic_id_date in enumerate(response.json()[:count_photo]):
        image_id = epic_id_date['image']
        aDate = datetime.date.fromisoformat(epic_id_date['date'].split(' ')[0])
        formatted_date = aDate.strftime("%Y/%m/%d")
        second_epic_nasa_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{image_id}.png'
        response = requests.get(second_epic_nasa_url, params=payload)
        response.raise_for_status()
        download_pictures(
            response.url,
            path_to_pictures,
            f'epic_nasa_{epic_photo_number}{get_file_extension(response.url)}',
        )


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(
        description="Программа для скачивания эпичных фото земли от NASA"
    )
    parser.add_argument("--url", help="Ссылка на скачивание")
    args = parser.parse_args()
    path_to_pictures = './images/'
    epic_nasa_payload = {
        'api_key': nasa_api_key,
    }
    count_epic_photo = 2
    if args.url:
        try:
            fetch_epic_nasa_launch(
                epic_nasa_payload,
                count_epic_photo,
                path_to_pictures,
                args.url,
            )
        except requests.exceptions.HTTPError as e:
            print(e.response.status_code)
    else:
        try:
            fetch_epic_nasa_launch(
                epic_nasa_payload,
                count_epic_photo,
                path_to_pictures,
            )
        except requests.exceptions.HTTPError as e:
            print(e.response.status_code)
