from settings import PATH, start_date, end_date
from os import path, mkdir

    
def build_dir():
    dir_name = str(start_date) + 'to' + str(end_date)
    dir = path.join(PATH, dir_name)
    if path.exists(dir):
        pass
    else:
        mkdir(dir)
    return dir
