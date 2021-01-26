from modules.settings import WALL

class Coor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

    def set(self, x, y):
        self.x, self.y = x, y

    def move(self, direc):
        if direc == 0:  # top
            return Coor(self.x - 1, self.y)

        if direc == 1:  # right
            return Coor(self.x, self.y + 1)

        if direc == 2:  # down
            return Coor(self.x + 1, self.y)

        return Coor(self.x, self.y - 1)  # left

    def euclid(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def isValidMove(self, maze):
        n_row, n_col = maze.shape
        return self.x >= 0 and self.x < n_row and self.y >= 0 and self.y < n_col and maze[self.get()] != WALL 
    
    def rangeCoor(self, other):
        x = sorted(self.x, other.x)
        y = sorted(self.y, other.y)
        
        return Coor(x[0], x[1] + 1), Coor(y[0], y[1] + 1)
    
    def copy(self):
        return Coor(self.x, self.y)
    
    def __str__(self):
        return f'({self.x} - {self.y})'


class Point:
    def __init__(self, id, coor):
        self.id = id
        self.coor = coor


class Edge:
    def __init__(self, start, end, feed):
        self.start = start
        self.end = end
        self.feed = feed
        self.weight = self.start.euclid(self.end)
