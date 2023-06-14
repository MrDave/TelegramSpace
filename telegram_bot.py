import telegram
from file_functions import load_token


token = load_token("TG_BOT_TOKEN")
bot = telegram.Bot(token)

chat_id = "@DaveSpacePhotos"

with open("images/nasa_apod_0.jpg", "rb") as file:
    bot.send_document(chat_id=chat_id, document=file)
