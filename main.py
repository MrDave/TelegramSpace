import requests
from pathlib import Path


def download_picture(url, path):

    response = requests.get(url)
    response.raise_for_status()

    with open(path, "wb") as file:
        file.write(response.content)


def get_spacex_pictures(launch_id="latest"):

    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()

    pictures = response.json()["links"]["flickr"]["original"]
    return pictures


def main():
    Path("images/").mkdir(exist_ok=True)

    for number, picture in enumerate(get_spacex_pictures("5eb87d42ffd86e000604b384")):
        download_picture(picture, f"images/spacex_{number}.jpg")


if __name__ == "__main__":

    main()
