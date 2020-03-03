from config import save_path
import os

def manage_path(save_path):
    if os.path.isdir(save_path):
        pass
    else:
        os.makedirs(save_path)