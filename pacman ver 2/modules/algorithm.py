import numpy as np
from queue import Queue
from modules.settings import PATH, WALL
from modules.util_classes import Coor

class Algorithm:
    def __init__(self, maze, source, target):
        self.maze = maze.copy()
        self.source = source
        self.target = target
        
    def getPath(self, visited):
        coor = self.target
        path = []
        
        while coor.get() != (-1, -1):
            path.append(coor)
            coor = visited[coor.get()]
            
        return path[::-1]

    def bfs(self):
        queue = Queue()
        queue.put(self.source)
        visited = {self.source.get(): Coor(-1, -1)}
        
        while not queue.empty():
            u = queue.get()
            
            if u == self.target:
                return self.getPath(visited)
            
            for direc in range(4):
                v = u.move(direc)
                
                if v < self.maze.shape and self.maze[v.get()] != WALL and visited.get(v.get()) is None:
                    queue.put(v)
                    visited[v.get()] = u
                    
