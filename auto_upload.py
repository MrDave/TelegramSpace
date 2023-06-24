from dotenv import load_dotenv
from file_functions import get_image_paths
from random import shuffle
from telegram.error import NetworkError
from time import sleep
from upload_telegram_picture import upload_image
import argparse
import os


def main():
    load_dotenv()
    token = os.environ["TG_BOT_TOKEN"]
    chat_id = os.environ["TG_CHANNEL_ID"]
    try:
        default_time = os.environ["WAIT_TIME"]
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
    network_error_counter = 0
    while True:
        shuffle(images)
        try:
            for image in images:
                upload_image(image, token, chat_id)
                sleep(sending_frequency)
                network_error_counter = 0
        except NetworkError:
            print(f"Network Error! I wait {5 ** network_error_counter} seconds")
            sleep(5 ** network_error_counter)
            if network_error_counter < 4:
                network_error_counter += 1


if __name__ == "__main__":
    main()
