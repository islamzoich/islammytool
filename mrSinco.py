import base64
import marshal
import zlib

def decrypt_file():
    try:
        # تحديد مسار الملف المشفر
        input_file = 'encrypted_example.txt'  # ضع اسم الملف المشفر الخاص بك هنا

        with open(input_file, 'rb') as file:
            encoded_content = file.read()

        decoded_content = base64.b85decode(encoded_content)
        decompressed_content = zlib.decompress(decoded_content)
        unmarshalled_content = marshal.loads(decompressed_content)

        # تحديد مسار الملف الذي سيتم حفظ النص المفكوك فيه
        output_file = 'decrypted_example.txt'  # ضع اسم الملف الذي ترغب في حفظ النص المفكوك فيه هنا

        with open(output_file, 'w') as decrypted_file:
            decrypted_file.write(unmarshalled_content)

        print(f'Decryption completed. Output file: {output_file}')
    except Exception as e:
        print(f'Error: {e}')

# تنفيذ الأداة
decrypt_file()
