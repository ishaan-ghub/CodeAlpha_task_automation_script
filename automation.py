import os
import shutil

try:
    target_folder = input("Enter path of the folder in which the files are located: ")
    extensions = {item.split('.')[1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}

    for extension in extensions:
        if not os.path.exists(os.path.join(target_folder, extension)):
            os.mkdir(os.path.join(target_folder, extension))
            
    for item in os.listdir(target_folder):
        if os.path.isfile(os.path.join(target_folder, item)):
            file_extension = item.split('.')[-1]
            shutil.move(os.path.join(target_folder, item), os.path.join(target_folder,file_extension, item))
except FileNotFoundError:
    print("Please enter a valid path to folder")