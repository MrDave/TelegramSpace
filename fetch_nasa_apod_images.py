import argparse
import requests
from file_functions import download_image
from file_functions import get_file_extension
from contextlib import suppress
import os
from dotenv import load_dotenv
from pathlib import PurePath


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Download NASA's Astronomy Picture of the Day"
    )

    parser.add_argument(
        "-c",
        "--count",
        help="download multiple random APOD's",
        type=int
    )
    args = parser.parse_args()
    token = os.getenv("NASA_TOKEN", default="DEMO_KEY")

    count = args.count

    downloading_path = os.getenv("DOWNLOADING_PATH", default="images")

    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": token,
        "count": count,
        "thumbs": True
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    image_responses = response.json()
    if isinstance(image_responses, dict):
        image_responses = [image_responses]
    images = []

    for image in image_responses:
        with suppress(KeyError):
            images.append(image.get("thumbnail_url", image["url"]))

    for number, image in enumerate(images):
        extension = get_file_extension(image)
        path = PurePath(downloading_path).joinpath(f"nasa_apod_{number}{extension}")
        download_image(image, path, downloading_path)


if __name__ == "__main__":
    main()
