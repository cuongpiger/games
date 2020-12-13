from json import dump, load

from PySide2.QtGui import QPixmap

from modules.maps import maps



def write_json_file(path, data):
    with open(path, 'w') as writer:
        dump(data, writer)


def read_json_file(path):
    try:
        with open(path) as reader:
            return load(reader)
    except:
        return None


def load_qpixmap(path):
    return QPixmap(path)


def get_map(maze_id):
    return maps[maze_id].copy()
