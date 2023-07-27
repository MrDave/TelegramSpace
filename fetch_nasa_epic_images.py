import argparse
import requests
import datetime
from file_functions import download_image
import os
from dotenv import load_dotenv
from pathlib import PurePath


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Download NASA's Earth Polychromatic Imaging Camera image(s)"
    )
    parser.add_argument(
        "-c",
        "--count",
        help="number of images to download",
        type=int,
        default=1,
        choices=range(1, 20),
        metavar="[1-20]"
    )
    args = parser.parse_args()
    token = os.getenv("NASA_TOKEN", default="DEMO_KEY")

    count = args.count

    save_folder = os.getenv("SAVE_FOLDER", default="images")

    api_url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": token
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()

    images = response.json()[:count]

    for number, image in enumerate(images):
        image_date = datetime.datetime.fromisoformat(image["date"]).strftime("%Y/%m/%d")
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image['image']}.png"
        params = {
            "api_key": {token},
        }
        path = PurePath(save_folder).joinpath(f"nasa_epic_{number}.png")
        download_image(image_url, path, params=params)


if __name__ == "__main__":
    main()
