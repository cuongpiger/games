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


class Edge:
    def __init__(self, start, end, feed):
        self.start = start
        self.end = end
        self.feed = feed
        self.weight = self.start.euclid(self.end)
