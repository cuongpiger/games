from json import dump, load

import numpy as np

from PySide2.QtGui import QPixmap

from modules.boards import boards


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __str__(self):
        return self.x, self.y



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


def get_board(maze_id):
    return boards[maze_id].copy()


def init_matrix_path(no_rows, no_cols):
    return [[-1] * no_cols for _ in range(no_rows)]


def hash_function(arr_state):
    return hash(tuple(arr_state))
    

def make_flat(board):
    return board.flatten()


def create_ending_state_hvalue(arr_state):
    arr = arr_state.copy()
    arr[(arr == 2) | (arr == 3)] = 1 # ending state don't contain any feed and pacman on the board

    return hash_function(arr)

def get_pacman_pos(arr_state):
    return int(np.where(arr_state == 3)[0][0])


MOVE = (Pos(-1, 0), Pos(0, 1), Pos(1, 0), Pos(0, -1))

def can_move(board, pacman_pos, direc, no_rows, no_cols):
    pos_pacman = Pos(pacman_pos // no_rows, pacman_pos % no_rows)
    pos = pos_pacman + MOVE[direc]
    pos = Pos(pos[0], pos[1])

    if pos.x < 0 or pos.x >= no_rows or pos.y < 0 or pos.y >= no_cols:
        return False, None

    return board[pos.x][pos.y] != 0, pos

def check_is_ending_state(arr_state, ending_state_hvalue):
    state = arr_state.copy()
    state[state == 3] = 1

    return hash_function(state) == ending_state_hvalue