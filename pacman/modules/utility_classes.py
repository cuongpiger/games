MOVE = ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1))

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

    def __mul__(self, other):
        return Pos(self.x * other, self.y * other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'({self.x},{self.y})'

    def move(self, direction):
        if direction == 0: # top
            return Pos(self.x + MOVE[0][0], self.y + MOVE[0][1])
        elif direction == 1: # right
            return Pos(self.x + MOVE[1][0], self.y + MOVE[1][1])
        elif direction == 2: # down
            return Pos(self.x + MOVE[2][0], self.y + MOVE[2][1])
        else: # left
            return Pos(self.x + MOVE[3][0], self.y + MOVE[3][1])
