import os
import app


def list_files(path):
    uploads = os.path.join(app.app.root_path, path)
    print(os.listdir(uploads))
    return os.listdir(uploads)
