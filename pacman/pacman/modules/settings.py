from modules.ultility_functions import read_json_file


class WindowSettings:
    def __init__(self):
        self.width = 811
        self.height = 355
        self.title = 'Pacman'
        self.icon = r'data/images/pacman.ico'
        self.cb_mazes = read_json_file(r'data/text/maze_info.json')
