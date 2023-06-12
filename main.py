import requests
import os
from urllib import parse
from pathlib import Path


def download_picture(url, path):

    response = requests.get(url)
    response.raise_for_status()

    with open(path, "wb") as file:
        file.write(response.content)


def fetch_spacex_pictures(launch_id="latest"):

    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()

    pictures = response.json()["links"]["flickr"]["original"]

    for number, picture in enumerate(pictures):
        download_picture(picture, f"images/spacex_{number}.jpg")


def get_file_extension(url):
    url_path = parse.urlsplit(url)
    file_extension = os.path.splitext(url_path.path)[1]
    return file_extension


def main():
    Path("images/").mkdir(exist_ok=True)

    fetch_spacex_pictures("5eb87d42ffd86e000604b384")


if __name__ == "__main__":

    main()
