import os
import datetime

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def current_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
