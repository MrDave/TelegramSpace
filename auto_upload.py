from upload_telegram_picture import upload_image
from file_functions import load_token
from file_functions import get_image_paths
import argparse
from random import shuffle
from time import sleep

try:
    default_time = load_token("WAIT_TIME")
except KeyError:
    default_time = 14400

parser = argparse.ArgumentParser(
    description="upload an image from \"images\" folder every 4 hours"
)
parser.add_argument(
    "-t",
    "--time",
    help="set how often (in seconds) an image is uploaded",
    type=int,
    default=default_time
)

args = parser.parse_args()
sending_frequency = args.time

images = get_image_paths()

while True:
    shuffle(images)
    for image in images:
        upload_image(image)
        sleep(sending_frequency)