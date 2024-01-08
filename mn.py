import os
import time

def create_large_file(file_path, size_mb):
    with open(file_path, 'wb') as file:
        file.write(b'\0' * (size_mb * 1024 * 1024))

output_directory = os.getcwd()  # يحصل على المسار الحالي للعمل
file_name_prefix = 'large_file'
file_size_mb = 70
num_files = 50
interval_seconds = 1

try:
    for count in range(1, num_files + 1):
        file_name = f"{file_name_prefix}_{count}.dat"
        file_path = os.path.join(output_directory, file_name)
        create_large_file(file_path, file_size_mb)
        print(f"Created file: {file_path}")
        time.sleep(interval_seconds)
except KeyboardInterrupt:
    print("تم إيقاف إنشاء الملفات.")
