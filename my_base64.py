import base64

def encrypt_file():
    try:
        input_file = input("Enter the path of the input text file: ")
        with open(input_file, 'rb') as file:
            content = file.read()
            encoded_content = base64.b64encode(content)

        output_file = input("Enter the path for the encrypted output file: ")
        with open(output_file, 'wb') as encrypted_file:
            encrypted_file.write(encoded_content)

        print(f'Encryption completed. Output file: {output_file}')
    except Exception as e:
        print(f'Error: {e}')

# Usage
encrypt_file()
