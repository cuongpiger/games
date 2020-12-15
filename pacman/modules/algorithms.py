import numpy as np
from queue import Queue
from modules.game_state import GameState
from modules.settings import GameSettings
from modules.utility_classes import Pos
from modules.utility_functions import (
    init_ending_state_hvalue,
    check_is_ending_state
)


gameSt = GameSettings()


class Algorithm:
    def __init__(self, start_state):
        self.start_state = start_state
        self.no_rows = start_state.state.shape[0]
        self.no_cols = start_state.state.shape[1]
        self.ending_state_hvalue = init_ending_state_hvalue(start_state.state)
        self.path = None


    def breadth_first_search(self, start_state, ending_pos):
        states = {}
        states[start_state.hvalue] = start_state
        queue = Queue()
        queue.put(start_state)

        while not queue.empty():
            state = queue.get()

            if state.pacman_pos == ending_pos:
                return state, self.get_path(states, state.hvalue)

            for direction in range(4):
                new_pacman_pos = state.pacman_pos.move(direction)

                if state.can_move(new_pacman_pos):
                    child_state = GameState(state.state, new_pacman_pos, state.hvalue)
                    child_state.update(state.pacman_pos)

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

        return np.array(path[::-1])


    def bfs_on_board(self):
        state = self.start_state
        path = []
        feed_pos = state.get_one_food_pos()

        while feed_pos is not None:
            new_state, new_path = self.breadth_first_search(state, feed_pos)

            state = new_state
            state.prev_hvalue = ''

            path.append(new_path)
            feed_pos = state.get_one_food_pos()

        self.format_path(path)


    def format_path(self, path):
        res = [self.start_state]
        
        for states in path:
            for i in range(1, len(states)):
                res.append(states[i])

        self.path = np.array(res)

    
    def get_moves(self):
        moves = []

        for i in range(1, len(self.path)):
            pos = self.path[i].pacman_pos - self.path[i-1].pacman_pos
            moves.append(pos)

        return np.array(moves)


    def print_path(self):
        for state in self.path:
            print(state.state, '\n')

            





