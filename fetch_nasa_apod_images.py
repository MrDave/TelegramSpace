import argparse
import requests
from file_functions import load_token
from file_functions import download_image
from file_functions import get_file_extension
from contextlib import suppress

parser = argparse.ArgumentParser(
    description="Download NASA's Astronomy Picture of the Day"
)
parser.add_argument(
    "-t",
    "--token",
    help="use personal NASA API Key token",
    action="store_true"
)
parser.add_argument(
    "-c",
    "--count",
    help="download multiple random APOD's",
    type=int
)
args = parser.parse_args()
token = "DEMO_KEY"
if args.token:
    token = load_token("NASA_TOKEN")

count = args.count

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