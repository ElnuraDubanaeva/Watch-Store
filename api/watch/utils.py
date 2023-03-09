import os
from datetime import datetime


def path_and_rename(instance, filename):
    now = datetime.now()
    ext = filename.split(".")[-1]
    upload_to = "watch_image"
    filename = f'{instance.watch_name}{now.strftime("%d-%m-%Y")}.{ext}'
    return os.path.join(upload_to, filename)
