from modules.util_functions import hashFunction
from modules.settings import PACMAN, PATH

class GameState:
    def __init__(self, maze, pacman_coor, parent_hvalue):
        self.pacman_coor = pacman_coor
        self.parent_hvalue = parent_hvalue
        self.maze = maze.copy()
        self.maze[self.pacman_coor.get()] = PACMAN
        
    def update(self, coor1, coor2, pacman_coor, parent_hvalue):
        self.maze[coor1.x:coor1.y, coor2.x:coor2.y] = PATH
        self.maze[self.pacman_coor.get()] = PATH
        self.maze[pacman_coor.get()] = PACMAN
        self.pacman_coor = pacman_coor
        self.parent_hvalue = parent_hvalue
        
    def checkEndingState(self, ending_hvalue):
        self.maze[self.pacman_coor.get()] = PATH
        return hashFunction(self.maze) == ending_hvalue
    
    def copy(self):
        return GameState(self.maze, self.pacman_coor.copy(), self.parent_hvalue)