from json import load


def read_json_file(path):
    try:
        with open(path) as reader:
            return load(reader)
    except:
        return None


class WindowSettings:
    def __init__(self):
        self.width = 811
        self.height = 355
        self.title = 'Pacman'
        self.icon = r'data/images/pacman.ico'
        self.feed_density = (0.01, 1.)
        self.pacman_speed = (1, 5)
        self.cb_mazes = read_json_file(r'data/text/maze_info.json')
        self.cb_algorithms = read_json_file(r'data/text/algorithms_info.json')


class GameSettings:
    def __init__(self):
        self.wall = 0
        self.path = 1
        self.pacman = 2
        self.feed = 3
        