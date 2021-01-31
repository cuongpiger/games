import numpy as np
from queue import Queue, LifoQueue, PriorityQueue
from modules.settings import WALL, FOOD
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

    def bfs(self, heuristic=None):
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
    
    def dfs(self, heuristic=None):
        stack = LifoQueue()
        stack.put(self.source)
        visited = {self.source.get(): Coor(-1, -1)}
        
        while not stack.empty():
            u = stack.get()
            
            if self.maze[u.get()] == FOOD:
                return (self.getPath(visited, u), u)
            
            keeper = np.zeros(4, dtype=bool)
            while keeper.sum() != 4:
                direc = np.random.randint(4)
                
                if keeper[direc] == True:
                    continue
                
                v = u.move(direc)
                keeper[direc] = True

                if v < self.maze.shape and self.maze[v.get()] != WALL and visited.get(v.get()) is None:
                    stack.put(v)
                    visited[v.get()] = u
                    
        return None
                
    def dijkstra(self, heuristic=None):
        pqueue = PriorityQueue()
        pqueue.put((0, self.source.get()))
        dist = np.full(self.maze.shape, np.inf)
        dist[self.source.get()] = 0.
        visited = {self.source.get(): Coor(-1, -1)}
        
        while not pqueue.empty():
            w, u = pqueue.get()
            u = Coor(u[0], u[1])
            
            if self.maze[u.get()] == FOOD:
                return (self.getPath(visited, u), u)
            
            for direc in range(4):
                v = u.move(direc)
                
                if v < self.maze.shape and self.maze[v.get()] != WALL and w + 1 < dist[v.get()]:
                    dist[v.get()] = w + 1
                    visited[v.get()] = u
                    pqueue.put((w + 1, v.get()))
                    
        return None
        
    def aStar(self, heuristic):
        pqueue = PriorityQueue()
        pqueue.put((0, 0, self.source.get()))
        dist = np.full(self.maze.shape, np.inf)
        dist[self.source.get()] = 0
        visited = {self.source.get(): Coor(-1, -1)}
        mask = np.where(self.maze == FOOD)
        
        if not len(mask[0]):
            return None
        
        i = np.random.randint(len(mask[0]))
        target = Coor(mask[0][i], mask[1][i])
        
        while not pqueue.empty():
            f, d, u = pqueue.get()
            u = Coor(u[0], u[1])
            
            if u == target:
                return (self.getPath(visited, u), u)
            
            for direc in range(4):
                v = u.move(direc)
                calcDist = getattr(v, heuristic)
                
                new_d = d + 1
                new_h = calcDist(target)
                new_f = new_d + new_h
                
                if v < self.maze.shape and self.maze[v.get()] != WALL and new_f < dist[v.get()]:
                    visited[v.get()] = u
                    dist[v.get()] = new_f
                    pqueue.put((new_f, new_d, v.get()))