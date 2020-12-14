import numpy as np
from queue import Queue
from modules.game_state import GameState
from modules.utility_classes import Pos
from modules.utility_functions import (
    init_ending_state_hvalue,
    check_is_ending_state
)


class Algorithm:
    def __init__(self, start_state):
        self.start_state = start_state
        self.no_rows = start_state.state.shape[0]
        self.no_cols = start_state.state.shape[1]
        self.ending_state_hvalue = init_ending_state_hvalue(start_state.state)


    def breadth_first_search(self):
        start_state = self.start_state
        states = {}
        states[start_state.hvalue] = start_state
        queue = Queue()
        queue.put(start_state)

        while not queue.empty():
            state = queue.get()
            
            if check_is_ending_state(state.state, state.pacman_pos, self.ending_state_hvalue):
                return np.array(self.get_path(states, state.hvalue))

            for direction in range(4): # top, right, down, left
                new_pacman_pos = state.pacman_pos.move(direction)

                if state.can_move(new_pacman_pos):
                    child_state = GameState(state.state, new_pacman_pos, state.hvalue)
                    child_state.update(state.pacman_pos, direction)

                    if states.get(child_state.hvalue) == None:
                        states[child_state.hvalue] = child_state
                        queue.put(child_state)


    def get_path(self, states, last_state_hvalue):
        path = []
        key = last_state_hvalue

        while True:
            state = states.get(key)

            if state.prev_hvalue == '':
                path.append(state)
                break
            
            path.append(state)
            key = state.prev_hvalue

        return path[::-1]


