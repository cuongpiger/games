from pygame.math import Vector2 as vt
from queue import Queue

from modules.game_state import *
from modules.utility_functions import hash_function, make_flat, create_ending_state_hvalue, can_move, check_is_ending_state, Pos, MOVE


class Algorithm:
    def __init__(self, board):
        self.board = board
        self.no_rows = board.shape[0]
        self.no_cols = board.shape[1]



    def breadth_first_search(self):
        arr_state = make_flat(self.board)
        start_state = GameState(arr_state, -1)
        ending_state_hvalue = create_ending_state_hvalue(arr_state)
        queue = Queue()
        queue.put(start_state)
        path = {}
        path[start_state.hash_value] = -1 # current game state, previous game state hash value
        cnt = 1
        
        while not queue.empty():
            current_state = queue.get() # current state array

            if check_is_ending_state(current_state.arr_state, ending_state_hvalue):
                return self.get_path(path, current_state.hash_value, start_state)

            for direc in range(4):
                check, future_pacman_pos = can_move(self.board, current_state.pacman_pos, direc, self.no_rows, self.no_cols)

                if check:
                    future_state = current_state.arr_state.copy()
                    future_state[current_state.pacman_pos] = 1
                    future_state[future_pacman_pos.x * self.no_cols + future_pacman_pos.y] = 3
                    future_hvalue = hash_function(future_state)

                    if path.get(future_hvalue) == None:
                        new_state = GameState(future_state, current_state.hash_value)
                        path[future_hvalue] = current_state
                        queue.put(new_state)
                        cnt += 1

        print('OKKKKKKKKKKKKKKKKKKKKKKKKK', cnt)

    
    def get_path(self, path, last_hvalue, start_state):
        res = []
        key = last_hvalue
        i = 0

        while i < 10:
            obj = path.get(key)
            res.append(obj)

            if obj.prev_hvalue == -1:
                break
            else:
                key = obj.prev_hvalue

            i += 1

        return res


