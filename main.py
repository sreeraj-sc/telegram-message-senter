import telegram
from telegram.ext import Updater

# Replace the following values with your own Telegram API credentials
BOT_TOKEN = 'your_bot_token'
CHAT_ID = 'your_chat_id'

def send_file(bot, file_path):
    with open(file_path, 'rb') as f:
        bot.send_document(chat_id=CHAT_ID, document=f)

if __name__ == '__main__':
    # Initialize the Telegram bot
    bot = telegram.Bot(token=BOT_TOKEN)

    # Send a file
    send_file(bot, '/path/to/your/file')

