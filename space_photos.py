import requests
import os
import datetime
from pathlib import Path
from urllib.parse import urlparse
from dotenv import load_dotenv
from fetch_EPIC_nasa_images import fetch_epic_nasa_launch
from fetch_nasa_images import fetch_nasa_launch
from fetch_spacex_images import fetch_spacex_launch
from function_for_download_pictures import download_pictures


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    path = Path("/home/maksim/python_projects/space_images/images")
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
