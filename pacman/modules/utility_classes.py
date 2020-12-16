MOVE = ((-1, 0), (0, 1), (1, 0), (0, -1))

'''
- Class dùng để truy cập vào các index trên một board
'''
class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'({self.x},{self.y})'

    def get(self):
        return (self.x, self.y)

    def swap(self):
        return Pos(self.y, self.x)

    def move(self, direction):
        if direction == 0: # top
            return Pos(self.x + MOVE[0][0], self.y + MOVE[0][1])
        elif direction == 1: # right
            return Pos(self.x + MOVE[1][0], self.y + MOVE[1][1])
        elif direction == 2: # down
            return Pos(self.x + MOVE[2][0], self.y + MOVE[2][1])
        else: # left
            return Pos(self.x + MOVE[3][0], self.y + MOVE[3][1])

    def get_angel(self):
        if self.x == 0:
            return 0 if self.y > 0 else 180
        else:
            return 270 if self.x > 0 else 90


class Location:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other):
        return (int(self.x) == int(other.x)) and (int(self.y) == int(other.y))

    def move(self, pos, speed):
        if pos.x != 0:
            return Location((self.x + pos.x)*speed, self.y)
        else:
            return Location(self.x, (self.y + pos.y)*speed)

