import numpy as np
from queue import Queue
from modules.settings import PATH, WALL, FOOD
from modules.util_classes import Coor

class Algorithm:
    def __init__(self, maze, source):
        self.maze = maze.copy()
        self.source = source
        
    def getPath(self, visited, food):
        coor = food
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
            
            if self.maze[u.get()] == FOOD:
                return (self.getPath(visited, u), u)
            
            for direc in range(4):
                v = u.move(direc)
                
                if v < self.maze.shape and self.maze[v.get()] != WALL and visited.get(v.get()) is None:
                    queue.put(v)
                    visited[v.get()] = u
                    
        return None
                    
