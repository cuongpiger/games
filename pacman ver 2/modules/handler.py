from modules.util_functions import hashFunction
from modules.settings import PACMAN, PATH, FOOD, WALL
from modules.algorithm import Algorithm
from queue import Queue
import numpy as np

class Handler:
    def __init__(self, maze, pacman_coor, algorithm, heuristic):
        self.maze = maze.copy()
        self.pacman_coor = pacman_coor.copy()
        self.algorithm = algorithm
        self.heuristic = heuristic
    
    def findClosestFood(self, maze, pacman_coor):
        queue = Queue()
        queue.put(pacman_coor)
        visited = {pacman_coor.get(): True}
        
        while not queue.empty():
            u = queue.get()
        
            if maze[u.get()] == FOOD:
                return u
            
            for direc in range(4):
                v = u.move(direc)
                
                if v < maze.shape and maze[v.get()] != WALL and visited.get(v.get()) == None:
                    queue.put(v)
                    visited[v.get()] = True
                    
        return None
    
    def getPath(self, lst_paths):
        res = [self.pacman_coor]
        
        for path in lst_paths:
            res += path[1:]
            
        return res
    
    def updateMaze(self, maze, source, path):
        maze[source.get()] = PATH
        for coor in path:
            maze[coor.get()] = PATH
            
    def solve(self):
        maze = self.maze.copy()
        source = self.pacman_coor
        target = self.findClosestFood(maze, source)
        lst_paths = []
        
        if not self.heuristic:
            while target is not None:
                path = getattr(Algorithm(maze, source, target), self.algorithm)()
                self.updateMaze(maze, source, path)
                lst_paths.append(path)
                source = target
                target = self.findClosestFood(maze, source)
                
        return self.getPath(lst_paths)
        
        