import numpy as np

from modules.utility_classes import Pos
from modules.utility_functions import hash_function
from modules.settings import GameSettings


gameSt = GameSettings()

class GameState():
    def __init__(self, state, pacman_pos, prev_state_hvalue):
        '''
        - `self.state` (np.matrix): trạng thái hiện tại của board, với 6 là wall, 7 là path, [0, 4] là vị trị của pacman đồng thời
            là hướng nhìn của pacman - lần lượt là top, right, down, left và stand
        - `self.pacman_pos` (Pos): postition hiện tại của pacman trên state
        - `self.hvalue` (str): hash value của `self.state`
        - `self.prev_hvalue` (str): hash value của parent state của `self.state`
        '''
        self.state = state.copy()
        self.pacman_pos = pacman_pos
        self.hvalue = hash_function(state)
        self.prev_hvalue = prev_state_hvalue

    def can_move(self, new_pacman_pos):
        no_rows, no_cols = self.state.shape

        if new_pacman_pos.x < 0 or new_pacman_pos.x >= no_rows or new_pacman_pos.y < 0 or new_pacman_pos.y >= no_cols:
            return False

        return self.state[new_pacman_pos.x, new_pacman_pos.y] != gameSt.wall

    def update(self, old_pacman_pos, pacman_direction):
        self.state[old_pacman_pos.x, old_pacman_pos.y] = gameSt.path
        self.state[self.pacman_pos.x, self.pacman_pos.y] = pacman_direction
        self.hvalue = hash_function(self.state)