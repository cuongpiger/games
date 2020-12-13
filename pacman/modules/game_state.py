import numpy as np

from modules.utility_functions import hash_function, get_pacman_pos, Pos


 # top, right, down, left


class GameState():
    def __init__(self, arr_state, prev_hvalue):
        self.arr_state = arr_state
        self.hash_value = hash_function(arr_state)
        self.pacman_pos = get_pacman_pos(arr_state)  
        self.prev_hvalue = prev_hvalue
    
    
    '''Only store feed and wall'''
    def create_raw_array(self):
        arr = self.make_flat()
        arr[arr == 3] = 1

        return arr

