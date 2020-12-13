from modules.utility_functions import get_map



class Game:
    def __init__(self, game_params):
        self.game_params = game_params
        self.map = get_map(self.game_params.maze_id)

        print(self.map)