import requests
import os
from urllib import parse
from pathlib import Path


def download_image(url, path, params=None):

    response = requests.get(url, params=params)
    response.raise_for_status()

    Path("images/").mkdir(exist_ok=True)

    with open(path, "wb") as file:
        file.write(response.content)


def get_file_extension(url):
    url_path = parse.urlsplit(url)
    file_extension = os.path.splitext(url_path.path)[1]
    return file_extension


def get_image_paths():

    image_paths = []
    for root, dirs, files in os.walk("images/"):
        for name in files:
            path = os.path.join(root, name)

            image_paths.append(path)

    return image_paths
