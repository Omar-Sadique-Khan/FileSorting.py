# 🤗 Let's get some sorting done!

# ⬇️ Imports
import os, shutil
from logging import exception
from pathlib import Path

# 📦 Variables - Global
PATH_DESKTOP = Path.home() / "Desktop" # Universal Path

# 📖 Define Sorting
CATEGORIES = {
    '_Images' : ['.jpg', '.jpeg', '.png'],
    '_Videos' : ['.mp4', '.mkv', '.avi', '.mov'],
    '_Docs'   : ['.pdf', '.docx', '.txt'],
    '_ZIPs'   : ['.zip', '.rar', '.7z'],
    '_Data'   : ['.csv', '.xlsx'],
    '_Code'   : ['.py', '.cpp', '.html', '.css', '.md', '.js']
} # ➕ Add more file formats according to your needs!

# ⚙️ Functions
def get_file_cat(filename):
    """ Finding Sorting Folder by name
    :param filename: Filename inside of downloads folder.
    :return:         Name of sorting folder. """
    # ❌ Ignore Soring Folders
    if filename.startswith('_'):
        return None

    # 🔍 Checks

    # 📂 Folders
    filepath = os.path.join(PATH_DESKTOP, filename)

    if os.path.isdir(filepath):
        return '_Folders'

    # 📃 Files
    else:
        file_extension = '.' + filename.split('.')[-1]

        # 👀 Looking for Category
        for cat, ext in CATEGORIES.items():
            if file_extension in ext:
                sorting_cat = cat
                return cat

        print(f'❓{file_extension} not supported. File: ({filepath})')
        return '_Others'

# 📗 Read all Files
def sort_desktop():
    all_files = os.listdir(PATH_DESKTOP)
    folders   = [f for f in all_files if os.path.isdir(os.path.join(PATH_DESKTOP, f)) and not f.startswith('_')]
    files     = [f for f in all_files if not os.path.isdir(os.path.join(PATH_DESKTOP, f))]

    #📋 Report to Console
    print('-' * 40)
    print('Scanning Desktop...')
    print(f'📂 Folders found: {len(folders)}')
    if files:
        print(f'📃 Files found: {len(files)}')
        print('\n--------------------Sorting--------------------')
    else:
        print('📃 Files found: 0.')
        print('\n🤷‍♂️ Noting to sort here...')

    for file in all_files:

        # Get File Categories
        dir_name = get_file_cat(file)

        if dir_name:

            # Create Soring Folders
            dir_filepath = os.path.join(PATH_DESKTOP, dir_name)
            if not os.path.exists(dir_filepath):
                os.makedirs(dir_filepath)

            # Define Old/New Paths
            old_path = os.path.join(PATH_DESKTOP, file)
            new_path = os.path.join(PATH_DESKTOP, dir_name, file)

            # Move Files
            try:
                shutil.move(old_path, new_path)
                print(f'➡️ {dir_name}/{file}')
            except Exception as e:
                print(f'❌ {dir_name}/{file} - {e}')

#🎯 Main
if __name__ == '__main__':
    sort_desktop()