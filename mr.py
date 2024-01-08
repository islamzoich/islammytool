 marshal

def decrypt_marshal():
    try:
        # اطلب من المستخدم إدخال مسار الملف المشفر
        input_file = input("Enter the path of the encrypted file: ")

        with open(input_file, 'rb') as file:
            data = file.read()

        code_object = marshal.loads(data)

        # اطلب من المستخدم إدخال اسم الملف الذي سيتم حفظ النص المفكوك فيه
        output_file = input("Enter the name of the file to save the decrypted text: ")

        with open(output_file, 'w') as decrypted_file:
            decrypted_file.write(code_object)

        print(f'Decryption completed. Output file: {output_file}')
    except Exception as e:
        print(f'Error: {e}')

# تنفيذ الأداة
decrypt_marshal()
