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
        self.create_feed_on_board()

        self.pacman_pos = self.create_pacman_pos()
        self.create_pacman_on_board()


    def get_path_pos(self):
        xs, ys = np.where(self.board == gameSt.path)
        return np.array([Pos(x, y) for x, y in zip(xs, ys)])


    def create_feed_pos(self):
        no_feed = max(int(round(len(self.path) * self.game_params.feed_density)), 1)
        return self.path[np.random.choice(len(self.path), no_feed, replace=False)]


    def create_pacman_pos(self):
        pos = self.path[np.random.choice(len(self.path), 1, replace=False)][0]
        
        if len(self.feed_pos) == 1:
            while self.board[pos.x, pos.y] == gameSt.feed:
                pos = self.path[np.random.choice(len(self.path), 1, replace=False)][0]

        return Pos(pos.x, pos.y)


    def create_feed_on_board(self):
        xs, ys = [pos.x for pos in self.feed_pos], [pos.y for pos in self.feed_pos]
        self.board[xs, ys] = gameSt.feed

    
    def create_pacman_on_board(self):
        self.board[self.pacman_pos.x, self.pacman_pos.y] = gameSt.pacman


    def bfs(self):
        start_state = GameState(self.board, self.pacman_pos, '')
        bfs = Algorithm(start_state)
        bfs.bfs_on_board()
        # bfs.print_path()

        return bfs.get_moves()
    


