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
    
    def copy(self):
        return Coor(self.x, self.y)
    
    def __lt__(self, other):
        if self.x < 0 or self.y < 0 or self.x >= other[0] or self.y >= other[1]:
            return False
        
        return True
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f'({self.x} - {self.y})'