import argparse
import requests
import os
from file_functions import download_image
from pathlib import PurePath
from dotenv import load_dotenv


def main():
    load_dotenv()
    downloading_path = os.getenv("DOWNLOADING_PATH", default="images")
    parser = argparse.ArgumentParser(
        description="Download images from SpaceX's launches"
    )
    parser.add_argument(
        "--id",
        help="ID of SpaceX launch. Latest by default",
        default="latest",
        type=str
    )
    args = parser.parse_args()
    launch_id = args.id

    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()

    images = response.json()["links"]["flickr"]["original"]

    for number, image in enumerate(images):
        path = PurePath(downloading_path).joinpath(f"spacex_{number}.jpg")
        download_image(image, path, downloading_path)


if __name__ == "__main__":
    main()
