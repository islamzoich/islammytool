from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

def encrypt_file_aes():
    print("***************************************")
    print("*                                     *")
    print("*  Welcome to Encryption Tool by Islam *")
    print("*                                     *")
    print("***************************************")

    input_file = input("Enter the name of the file to encrypt: ")
    output_file = input("Enter the name of the encrypted output file: ")

    # مفتاح ثابت (يجب تغييره إذا كان يتم نشر الأداة)
    encryption_key = b'\x01\x23\x45\x67\x89\xAB\xCD\xEF\xFE\xDC\xBA\x98\x76\x54\x32\x10'

    try:
        with open(input_file, 'rb') as file:
            plaintext = file.read()

        cipher = Cipher(algorithms.AES(encryption_key), modes.CFB(os.urandom(16)), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()

        # استخدام Base64 لتشفير النص
        encoded_ciphertext = base64.b64encode(ciphertext)

        with open(output_file, 'wb') as encrypted_file:
            encrypted_file.write(encoded_ciphertext)

        print("Encryption completed successfully.")
        print(f"Encrypted file saved as: {output_file}")
        print("***************************************")
    except Exception as e:
        print(f'Error: {e}')
        print("Encryption failed.")
        print("***************************************")

# استدعاء الدالة لتشفير ملف المستخدم
encrypt_file_aes()
