import numpy as np
from queue import Queue
from modules.util_classes import Coor, Point
from modules.settings import WALL, FLAG, FOOD, PATH


class Game:
    def __init__(self, game_params):
        self.game_params = game_params
        # read maze from *.txt file
        self.maze = np.loadtxt(self.game_params.maze, dtype=np.int8)
        self.pacman_coor = self.generatePacmanCoor()  # generate pacman's coordinate
        self.flags = self.getFlagsCoors()  # get coordinates of flag point in `self.maze`
        self.mask = self.createMaskMatrix()
        self.adj_matrix = self.createAdjacencyMatrix()
        self.generateFood()

    def generatePacmanCoor(self):
        """ Generate pacman's coordinate on the `self.maze`

        Returns:
            [Coor]: Pacman's coordinate
        """
        n_row, n_col = self.maze.shape
        pacman_coor = Coor(0, 0)

        while self.maze[pacman_coor.get()] == WALL:
            pacman_coor.set(np.random.randint(n_row), np.random.randint(n_col))

        self.maze[pacman_coor.get()] = FLAG
        return pacman_coor

    def generateFood(self):
        """ Generate feed's coordinates and set their value into `FOOD` on the `self.maze`
        """
        possibleCoor = np.where(
            self.maze != WALL)  # get all coordinates which pacman can arrive
        n_coor = len(possibleCoor[0])
        # the amount of feed is based on `feed_density`
        n_food = int(round(n_coor*self.game_params.feed_density))
        coors = np.arange(n_coor)
        np.random.shuffle(coors)
        self.maze[self.maze != WALL] = PATH
        self.maze[possibleCoor[0][:n_food], possibleCoor[1][:n_food]] = FOOD

    def getFlagsCoors(self):
        return [Point(i, Coor(coor[0], coor[1])) for i, coor in enumerate(zip(*np.where(self.maze == FLAG)))]

    def createMaskMatrix(self):
        n = len(self.flags)
        mask = np.full((n, n), -1)

        for flag in self.flags:
            mask[flag.coor.get()] = flag.id

        return mask

    def createAdjacencyMatrix(self):
        n = len(self.flags)
        adj_matrix = np.zeros((n, n), dtype=np.int8)
        visited = np.full(self.maze.shape, -1)
        visited[self.pacman_coor.get()] = -2
        queue = Queue()
        queue.put(self.pacman_coor)

        while not queue.empty():
            coor = queue.get()

            for direc in range(4):
                new_coor = coor.move(direc)

                while new_coor.isValidMove(self.maze) and visited[new_coor.get()] == -1:
                    visited[new_coor.get()] = -2

                    if self.maze[new_coor.get()] == FLAG:
                        queue.put(new_coor)
                        u = self.mask[coor.get()]
                        v = self.mask[new_coor.get()]
                        adj_matrix[u, v] = 1
                        adj_matrix[v, u] = 1

                        break

                    new_coor = new_coor.move(direc)

        return adj_matrix