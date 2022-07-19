import requests
import os
import datetime
from pathlib import Path
from urllib.parse import urlparse
from dotenv import load_dotenv


def download_pictures(url, path_to_pictures, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(f"{path_to_pictures}{filename}", 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch(url, path_to_pictures, flight_id='latest'):
    response = requests.get(url + flight_id)
    response.raise_for_status()
    spacex_photos = response.json()['links']['flickr']['original']
    for photo_number, photo in enumerate(spacex_photos):
        download_pictures(
            photo,
            path_to_pictures,
            f'spacex_{photo_number}{get_file_extension(photo)}'
        )


def fetch_nasa_launch(url, payload, path_to_pictures):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for photo_number, day_nasa_photo in enumerate(response.json()):
        download_pictures(
            day_nasa_photo['url'],
            path_to_pictures,
            f'nasa_{photo_number}{get_file_extension(day_nasa_photo["url"])}',
        )


def fetch_epic_nasa_launch(epic_nasa_url, payload, count_photo, path_to_pictures):
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


def get_file_extension(url):
    url_parts = urlparse(url)
    path_with_file_extension = url_parts.path
    path, file_extension = os.path.splitext(path_with_file_extension)
    return file_extension


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    path = Path("/home/maksim/python_projects/space_photos/images")
    path.mkdir(parents=True, exist_ok=True)
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    path_to_pictures = './images/'
    filename = 'space.jpeg'
    try:
        download_pictures(
            url,
            path_to_pictures,
            filename,
        )
    except requests.exceptions.HTTPError as e:
        print(e.response.status_code)
    flight_id = '5eb87d47ffd86e000604b38a'
    spacex_url = f"https://api.spacexdata.com/v5/launches/"
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    epic_nasa_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    nasa_payload = {
        'api_key': nasa_api_key,
        'count': 10
    }
    epic_nasa_payload = {
        'api_key': nasa_api_key,
    }
    count_epic_photo = 2
    try:
        fetch_epic_nasa_launch(
            epic_nasa_url,
            epic_nasa_payload,
            count_epic_photo,
            path_to_pictures,
        )
    except requests.exceptions.HTTPError as e:
        print(e.response.status_code)
    try:
        fetch_nasa_launch(
            nasa_url,
            nasa_payload,
            path_to_pictures,
        )
    except requests.exceptions.HTTPError as e:
        print(e.response.status_code)
    try:
        fetch_spacex_launch(
            spacex_url,
            path_to_pictures,
            flight_id=flight_id,
        )
    except requests.exceptions.HTTPError as e:
        print(e.response.status_code)
