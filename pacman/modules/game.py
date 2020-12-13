import numpy as np

from pygame.math import Vector2 as vt

from modules.utility_functions import get_board



class Game:
    def __init__(self, game_params):
        self.game_params = game_params
        self.board = get_board(self.game_params.maze_id)
        self.path = self.get_path_pos()
        self.feed_pos = self.create_feed_pos()
        self.pacman_pos = self.create_pacman_pos()
        
        self.create_feed_on_board()
        self.create_pacman_on_board()

        #print(self.board)

    
    '''Get cells' postition which not equal to 0'''
    def get_path_pos(self):
        posI, posJ = np.where(self.board != 0)
        return np.array(list(zip(posI, posJ)))


    '''Create feed'''
    def create_feed_pos(self):
        no_feed = int(round(len(self.path) * self.game_params.feed_density))
        return self.path[np.random.choice(len(self.path), no_feed, replace=False)]


    def create_pacman_pos(self):
        pos = self.path[np.random.choice(len(self.path), 1, replace=False)][0]
        return vt(pos[0], pos[1])


    '''Create feed on map'''
    def create_feed_on_board(self):
        posI, posJ = [i for i, _ in self.feed_pos], [j for _, j in self.feed_pos]
        self.board[posI, posJ] = 2

    
    def create_pacman_on_board(self):
        self.board[int(self.pacman_pos.x), int(self.pacman_pos.y)] = 3

