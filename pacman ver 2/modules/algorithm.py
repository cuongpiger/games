import numpy as np
from queue import Queue
from modules.settings import PATH, WALL
from modules.util_functions import hashFunction


class Algorithm:
    def __init__(self, maze, start, target):
        self.maze = maze
        self.pacman_coor = pacman_coor
        self.flags = flags
        self.mask = mask
        self.adj_matrix = adj_matrix

    def createEndingHashValue(self):
        maze = self.maze.copy()
        maze[maze != WALL] = PATH

        return hashFunction(maze)

    def getPath(self, visited, last_state):
        state = last_state
        path = []

        while state.parent_hvalue != None:
            path.append(state.pacman_coor)
            state = visited[state.parent_hvalue]
            
        path.append(state.pacman_coor)

        return path[::-1]

    def bfs(self):
        start_state = GameState(self.maze, self.pacman_coor, None)
        start_hvalue = hashFunction(start_state.maze)
        visited = {start_hvalue: start_state}
        ending = self.createEndingHashValue()
        queue = Queue()
        queue.put(start_state)

        while not queue.empty():
            state = queue.get()

            if state.checkEndingState(ending):
                print('>> go here')
                return self.getPath(visited, state)

            u = self.mask[state.pacman_coor.get()]
            for v in np.where(self.adj_matrix[u] != 0)[0]:
                new_state = state.copy()
                coor1, coor2 = self.flags[u].coor.rangeCoor(self.flags[v].coor)
                new_state.update(
                    coor1, coor2, self.flags[v].coor, hashFunction(state.maze))
                new_state_hvalue = hashFunction(new_state.maze)

                if visited.get(new_state_hvalue) == None:
                    visited[new_state_hvalue] = new_state
                    queue.put(new_state)


bfs = Algorithm.bfs