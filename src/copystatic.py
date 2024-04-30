import os
import shutil

def scan_directory(path, files, folders):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            folders.append(full_path)
            scan_directory(full_path, files, folders)  # Recursive call with the same lists
        else:
            files.append(full_path)

def empty_public():
    public_path = "/home/depood/workspace/github.com/depoods/staticsite/public"
    files = []
    folders = []
    scan_directory(public_path, files, folders)

    for file in files:
        if file.startswith(public_path):
            os.remove(file)  # Deletes each file

    for folder in reversed(folders):  # Reverse the order to delete deepest folders first
        if folder.startswith(public_path):
            os.rmdir(folder)  # Deletes each folder

def copy_to_public():
    static_path = "/home/depood/workspace/github.com/depoods/staticsite/static"
    public_path = "/home/depood/workspace/github.com/depoods/staticsite/public"
    files = []
    folders = []
    scan_directory(static_path, files, folders)

    for static_file in files:
        if static_file.startswith(static_path):
            # Extract the relative path of the file from static_path
            relative_path = static_file[len(static_path):]
            
            # Construct the destination file path by appending the relative path to public_path
            public_file = os.path.join(public_path, relative_path.strip("/"))
            
            # Ensure the directory exists. If not, create it.
            os.makedirs(os.path.dirname(public_file), exist_ok=True)
            
            # Copy the file from static to public
            shutil.copy(static_file, public_file)