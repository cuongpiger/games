from modules.settings import PATH
from modules.algorithm import Algorithm
import numpy as np


class Handler:
    def __init__(self, maze, pacman_coor, algorithm, heuristic):
        self.maze = maze.copy()
        self.pacman_coor = pacman_coor.copy()
        self.algorithm = algorithm
        self.heuristic = heuristic

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
        lst_paths = []

        if not self.heuristic:
            while True:
                res = getattr(Algorithm(maze, source), self.algorithm)()

                if res is None:
                    break

                self.updateMaze(maze, source, res[0])
                lst_paths.append(res[0])
                source = res[1]

        return self.getPath(lst_paths)
