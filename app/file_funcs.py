import os


def list_files(root_path, path):
    uploads = os.path.join(root_path, path)
    print(os.listdir(uploads))
    return os.listdir(uploads)
