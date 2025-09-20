import os
import shutil
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python file_organizer.py <folder_path>")

folder_path = sys.argv[1]

original_path = os.path.join(os.path.expanduser("~"), folder_path)
new_path = os.path.join(original_path, "OrganizedFiles")

if not os.path.exists(new_path):
    os.makedirs(new_path)

for filename in os.listdir(original_path):
    file_path = os.path.join(original_path, filename)

    if os.path.isfile(file_path):
        file_extension = filename.split(".")[-1].lower()
        folder_extension = os.path.join(new_path, file_extension)

        if not os.path.exists(folder_extension):
            os.makedirs(folder_extension)

        shutil.move(file_path, os.path.join(folder_extension, filename))

print("Files organized successfully.")
