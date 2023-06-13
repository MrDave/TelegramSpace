import argparse
import requests
import datetime
from file_functions import load_token
from file_functions import download_image


parser = argparse.ArgumentParser(
    description="Download NASA's Earth Polychromatic Imaging Camera image(s)"
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
    help="number of images to download",
    type=int,
    default=1,
    choices=range(1, 20),
    metavar="[1-20]"
)
args = parser.parse_args()
token = "DEMO_KEY"
if args.token:
    token = load_token("NASA_TOKEN")

count = args.count

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
