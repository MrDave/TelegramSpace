import telegram
from file_functions import get_image_paths
import argparse
from random import choice
import os
from dotenv import load_dotenv


def upload_image(image, bot_token, chat_id):
    bot = telegram.Bot(bot_token)
    with open(image, "rb") as file:
        bot.send_document(chat_id=chat_id, document=file)


def main():
    load_dotenv()
    token = os.environ["TG_BOT_TOKEN"]
    chat_id = os.environ["TG_CHANNEL_ID"]

    parser = argparse.ArgumentParser(description="Upload a random photo to Telegram channel")
    parser.add_argument(
        "-f",
        "--file",
        help="path of specific file to upload. Example: \"images/image.jpg\"",
        type=str
    )
    args = parser.parse_args()
    image = args.file

    if image is None:
        images = get_image_paths()
        image = choice(images)
    upload_image(image, token, chat_id)


if __name__ == "__main__":
    main()
