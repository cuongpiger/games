import numpy as np
from queue import Queue
from modules.util_classes import Coor
from modules.settings import WALL, FLAG, FOOD


class Game:
    def __init__(self, game_params):
        self.game_params = game_params
        self.maze = np.loadtxt(self.game_params.maze, dtype=np.int8) # read maze from *.txt file
        self.pacman_coor = self.generatePacmanCoor()  # generate pacman's coordinate
        self.flags = self.getFlagsCoors()  # get coordinates of flag point in `self.maze`
        self.generateFood()

        print(self.maze)

    def generatePacmanCoor(self):
        """ Generate pacman's coordinate on the `self.maze`

        Returns:
            [Coor]: Pacman's coordinate
        """
        n_row, n_col = self.maze.shape
        pacman_coor = Coor(0, 0)

        while self.maze[pacman_coor.get()] == WALL:
            pacman_coor.set(np.random.randint(n_row), np.random.randint(n_col))

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
        self.maze[possibleCoor[0][:n_food], possibleCoor[1][:n_food]] = FOOD

    def getFlagsCoors(self):
        return np.where(self.maze == FLAG)
    
    def createAdjacencyEdges(self):
        
