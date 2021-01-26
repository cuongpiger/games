import numpy as np
from queue import Queue
from modules.settings import PATH
from modules.util_functions import hashFunction
from modules.game_state import GameState

class Algorithm:
    def __init__(self, maze, pacman_coor, flags, mask, adj_matrix):
        self.maze = maze
        self.pacman_coor = pacman_coor
        self.flags = flags
        self.mask = mask
        self.adj_matrix = adj_matrix
        
    def createEndingMaze(self):
        maze = self.maze.copy()
        maze[maze != WALL] = PATH
        
        return maze
        
    def bfs(self):
        start_state = GameState(self.maze, self.pacman_coor, None)
        start_hvalue = hashFunction(start_state.maze)
        visited = {start_hvalue: start_state}
        ending = self.createEndingMaze()
        queue = Queue()
        queue.put(start_state)
        
        while not queue.empty():
            state = queue.get()
            
            if state.checkEndingState(ending):
                pass
            
            u = self.mask[state.pacman_coor.get()]
            for v in np.where(self.adj_matrix[u] != 0)[0]:
                new_state = state.copy()
                coor1, coor2 = self.flags[u].coor.rangeCoor(self.flags[v].coor)
                new_state.updateMaze(coor1, coor2, )
            
        