import numpy as np
from queue import Queue
from modules.util_classes import Coor
from modules.settings import WALL, FOOD, PATH, PACMAN
from modules.handler import Handler


class Game:
    def __init__(self, game_params):
        self.game_params = game_params
        self.maze = np.loadtxt(game_params.maze, dtype=np.int8) # read maze from *.txt file
        self.generateFood()
        self.generatePacman()

    def generatePacman(self):
        """ Generate pacman's coordinate on the `self.maze`

        Returns:
            [Coor]: Pacman's coordinate
        """
        n_row, n_col = self.maze.shape
        pacman_coor = Coor(0, 0)

        while self.maze[pacman_coor.get()] == WALL:
            pacman_coor.set(np.random.randint(n_row), np.random.randint(n_col))

        self.maze[pacman_coor.get()] = PACMAN
        self.pacman_coor = pacman_coor

    def generateFood(self):
        """ Generate feed's coordinates and set their value into `FOOD` on the `self.maze`
        """
        path_cells = np.where(self.maze == PATH)  # get all coordinates which pacman can arrive
        n_path_cells = len(path_cells[0]) # get the amount of path cells
        n_food_cells = max(int(round(n_path_cells*self.game_params.feed_density)), 2) # the amount of feed is based on `feed_density`
        path_cell_indices = np.arange(n_path_cells)
        np.random.shuffle(path_cell_indices)
        
        self.maze[path_cells[0][path_cell_indices[:n_food_cells]], path_cells[1][path_cell_indices[:n_food_cells]]] = FOOD
    
    def solve(self):
        handler = Handler(self.maze, self.pacman_coor, self.game_params.algorithm, self.game_params.heuristic)
        return handler.solve()
                
    def __str__(self):
        print(f'>> Pacman coor: {self.pacman_coor}')
        print(f'>> Maze:\n{self.maze}')
        
        return '\n'
            