import requests
import os
import datetime
import argparse
from dotenv import load_dotenv
from utils import get_file_extension
from utils import download_pictures
from pathlib import Path


def fetch_epic_nasa_launch(
    payload,
    count_photo,
    path_to_pictures,
     ):
    epic_nasa_url='https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(epic_nasa_url, params=payload)
    response.raise_for_status()
    for epic_photo_number, epic_id_date in enumerate(response.json()[:count_photo]):
        image_id = epic_id_date['image']
        a_date = datetime.datetime.fromisoformat(epic_id_date['date'])
        formatted_date = a_date.strftime("%Y/%m/%d")
        second_epic_nasa_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{image_id}.png'
        response = requests.get(second_epic_nasa_url, params=payload)
        response.raise_for_status()
        download_pictures(
            path_to_pictures,
            f'epic_nasa_{epic_photo_number}{get_file_extension(response.url)}',
            response.url,
        )


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(
        description="Программа для скачивания эпичных фото земли от NASA"
    )
    parser.add_argument("--num", type=int, default=10,
                        help="Количество фотографий для скачивания")    
    args = parser.parse_args()
    path_to_pictures = Path.cwd() / 'images'
    Path(path_to_pictures).mkdir(parents=True, exist_ok=True)
    epic_nasa_payload = {
        'api_key': nasa_api_key,
    }
    fetch_epic_nasa_launch(
        epic_nasa_payload,
        args.num,
        path_to_pictures,
    )
