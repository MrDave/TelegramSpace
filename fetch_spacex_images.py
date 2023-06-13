import argparse
import requests
from file_functions import download_image


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
    download_image(image, f"images/spacex_{number}.jpg")
