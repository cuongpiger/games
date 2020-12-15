import hashlib
from PySide2.QtGui import QPixmap
from modules.boards import boards
from modules.settings import GameSettings


gameSt = GameSettings()


def load_qpixmap(path):
    return QPixmap(path)


def get_board(maze_id):
    return boards[maze_id]

    
def hash_function(state):
    return hashlib.sha1(state.tobytes()).hexdigest()