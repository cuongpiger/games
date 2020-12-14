import numpy as np
from modules.utility_functions import get_board
from modules.utility_classes import Pos
from modules.settings import GameSettings
from modules.algorithms import Algorithm
from modules.game_state import GameState


gameSt = GameSettings()


class Game:
    def __init__(self, game_params):
        self.game_params = game_params
        self.board = np.matrix(get_board(game_params.maze_id))
        self.path = self.get_path_pos()
        self.feed_pos = self.create_feed_pos()
        self.pacman_pos = self.create_pacman_pos()
        
        self.create_feed_on_board()
        self.create_pacman_on_board()


    def get_path_pos(self):
        x, y = np.where(self.board == gameSt.path)
        return np.array(list(zip(x, y)))


    def create_feed_pos(self):
        no_feed = int(round(len(self.path) * self.game_params.feed_density))
        return self.path[np.random.choice(len(self.path), no_feed, replace=False)]


    def create_pacman_pos(self):
        pos = self.path[np.random.choice(len(self.path), 1, replace=False)][0]
        return Pos(pos[0], pos[1])


    def create_feed_on_board(self):
        x, y = [i for i, _ in self.feed_pos], [j for _, j in self.feed_pos]
        self.board[x, y] = gameSt.feed

    
    def create_pacman_on_board(self):
        self.board[self.pacman_pos.x, self.pacman_pos.y] = gameSt.pacman

    def bfs(self):
        start_state = GameState(self.board, self.pacman_pos, '')
        bfs = Algorithm(start_state)
        path = bfs.breadth_first_search()

        for obj in path:
            print(obj.state)
            print('_________________')
    


