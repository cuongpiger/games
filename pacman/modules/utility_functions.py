import numpy as np
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
    

def init_ending_state_hvalue(ori_state):
    state = ori_state.copy()
    state[(state == gameSt.feed) | (state <= gameSt.pacman)] = gameSt.path

    return hash_function(state)


def check_is_ending_state(ori_state, pacman_pos,ending_state_hvalue):
    state = ori_state.copy()
    state[pacman_pos.x, pacman_pos.y] = gameSt.path
    hvalue = hash_function(state)

    return hvalue == ending_state_hvalue