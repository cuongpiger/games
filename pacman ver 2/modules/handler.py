from modules.util_functions import hashFunction
from modules.settings import PACMAN, PATH, FOOD, WALL
from modules.algorithm import bfs
from queue import Queue
import numpy as np

class Handler:
    def __init__(self, maze, pacman_coor, algorithm, heuristic):
        self.maze = maze.copy()
        self.pacman_coor = pacman_coor.copy()
        self.algorithm = algorithm
        self.heuristic = heuristic
    
    def findClosestFood(self):
        queue = Queue()
        queue.put(self.pacman_coor)
        visited = np.zeros(self.maze.shape, dtype=bool)
        visited[self.pacman_coor.get()] = True
        
        while not queue.empty():
            u = queue.get()
            
            for direc in range(4):
                v = u.move(direc)
                
                if self.maze[u.get()] == FOOD:
                    return u
                
                if v < self.maze.shape and self.maze[v.get()] != WALL:
                    queue.put(v)
                    visited[v.get()] = True
                    
        return None
        
        
        
    def solve(self):
        total_food = np.sum(self.maze == FOOD)
        cur_food = 0
        state = self.maze
        source = self.pacman_coor
        target = self.pacman_coor
        
        if not self.heuristic:
            while target is not None:
                target = self.findClosestFood()
        
        