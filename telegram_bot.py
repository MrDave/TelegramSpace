import telegram
from file_functions import load_token


token = load_token("TG_BOT_TOKEN")
bot = telegram.Bot(token)

chat_id = load_token("TG_TEST_CHAT")
text = "There are some, who call me... Tim"
bot.send_message(chat_id=chat_id, text=text)
