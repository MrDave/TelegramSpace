import telegram
from file_functions import load_token
from file_functions import get_image_paths
import argparse
from random import choice
from time import sleep


def upload_image(image):

    token = load_token("TG_BOT_TOKEN")
    bot = telegram.Bot(token)

    chat_id = load_token("TG_CHANNEL_ID")

    with open(image, "rb") as file:
        bot.send_document(chat_id=chat_id, document=file)


def main():
    parser = argparse.ArgumentParser(description="Upload a random photo to Telegram channel")
    parser.add_argument(
        "-f",
        "--file",
        help="path of specific file to upload. Example: \"images\\image.jpg\"",
        type=str
    )
    args = parser.parse_args()
    image = args.file

    if image is None:
        images = get_image_paths()
        image = choice(images)
    upload_image(image)


if __name__ == "__main__":
    main()
