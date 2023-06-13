import requests
import os
from urllib import parse
from pathlib import Path
from dotenv import load_dotenv


def download_image(url, path):

    response = requests.get(url)
    response.raise_for_status()

    Path("images/").mkdir(exist_ok=True)

    with open(path, "wb") as file:
        file.write(response.content)


def get_file_extension(url):
    url_path = parse.urlsplit(url)
    file_extension = os.path.splitext(url_path.path)[1]
    return file_extension


def load_token(token):
    load_dotenv()
    return os.environ[token]
