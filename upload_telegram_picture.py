import telegram
from file_functions import load_token
from file_functions import get_image_paths
import argparse
from random import shuffle
from time import sleep


def upload_image(image):

    token = load_token("TG_BOT_TOKEN")
    bot = telegram.Bot(token)

    chat_id = load_token("TG_CHANNEL_ID")

    with open(image, "rb") as file:
        bot.send_document(chat_id=chat_id, document=file)


def main():

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


if __name__ == "__main__":
    main()
