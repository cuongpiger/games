import numpy as np
from queue import Queue
from modules.settings import PATH, WALL


class Algorithm:
    def __init__(self, maze, source, target):
        self.maze = maze.copy()
        self.source = source
        self.target = target
        
    def getPath(self, visited):
        coor = self.target.get()
        path = []
        
        while coor != (-1, -1):
            path.append(coor)
            coor = visited[coor]
            
        return path[::-1]

    def bfs(self):
        queue = Queue()
        queue.put(self.source)
        visited = {self.source.get(): (-1, -1)}
        
        while not queue.empty():
            u = queue.get()
            
            if u == self.target:
                return self.getPath(visited)
            
            for direc in range(4):
                v = u.move(direc)
                
                if v < self.maze.shape and self.maze[v.get()] != WALL and visited.get(v.get()) == None:
                    queue.put(v)
                    visited[v.get()] = u.get()
                    
