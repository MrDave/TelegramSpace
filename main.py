import requests
import os
from urllib import parse
from pathlib import Path
from dotenv import load_dotenv
from contextlib import suppress
import datetime


def download_image(url, path):

    response = requests.get(url)
    response.raise_for_status()

    with open(path, "wb") as file:
        file.write(response.content)


def fetch_spacex_images(launch_id="latest"):

    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()

    images = response.json()["links"]["flickr"]["original"]

    for number, image in enumerate(images):
        download_image(image, f"images/spacex_{number}.jpg")


def get_file_extension(url):
    url_path = parse.urlsplit(url)
    file_extension = os.path.splitext(url_path.path)[1]
    return file_extension


def fetch_nasa_apod_images(token="DEMO_KEY", count=None):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": token,
        "count": count,
        "thumbs": True
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    images_json = response.json()
    if type(response.json()) == dict:
        images_json = [response.json()]
    images = []

    for image in images_json:
        with suppress(KeyError):
            images.append(image.get("thumbnail_url", image["url"]))
    
    for number, image in enumerate(images):
        extension = get_file_extension(image)
        path = f"images/nasa_apod_{number}{extension}"
        download_image(image, path)


def fetch_nasa_epic_images(token, count=5):
    api_url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": token
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()

    images = response.json()[:count]

    for number, image in enumerate(images):
        image_date = datetime.datetime.fromisoformat(image["date"]).strftime("%Y/%m/%d")
        image_url = (
            f"https://api.nasa.gov/EPIC/archive/natural/"
            f"{image_date}/png/{image['image']}.png?api_key={token}"
        )
        path = f"images/nasa_epic_{number}.png"
        download_image(image_url, path)


def main():
    Path("images/").mkdir(exist_ok=True)
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    # fetch_spacex_images("5eb87d42ffd86e000604b384")
    # fetch_nasa_apod_images(nasa_token, 5)
    fetch_nasa_epic_images(nasa_token, 5)


if __name__ == "__main__":

    main()
