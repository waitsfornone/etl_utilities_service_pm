import os


def list_files(root_path, path):
    filepath_list = []
    uploads = os.path.join(root_path, path)
    for filename in os.listdir(uploads):
        filepath = uploads + '/' + filename
        filepath_list.append(filepath)
    return filepath_list
