import os
import shutil

def copy_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.getcwd()  # Директория, откуда была вызвана командная строка

    source_files = os.listdir(current_dir)
    for file in source_files:
        if file != 'library.py':
            source_path = os.path.join(current_dir, file)
            target_path = os.path.join(target_dir, file)
            shutil.copy2(source_path, target_path)

copy_files()
