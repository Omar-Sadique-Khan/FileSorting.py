# 🤗 Let's get some sorting done!

# ⬇️ Imports
import os
from fileinput import filename
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

    # 🔍 Checks

    # 📂 Folders
    filepath = os.path.join(PATH_DESKTOP, filename)

    if os.path.isdir(filepath):
        return None

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
for file in os.listdir(PATH_DESKTOP):
    cat = get_file_cat(file)

# Get File Categories

# Create Soring Folders

# Move Files

# Report Results

# Bonus: Create a CMD-Command