from modules.algorithms import Algorithm
from modules.utility_functions import get_board
from modules.parameters import GameParameters
from modules.game import Game
from modules.game_state import GameState
from modules.algorithms import Algorithm

maze_id, maze_img, maze_width, maze_height, algorithm = 0, 'data/images/mazes/maze_0.png', 840, 930, 'bfs'

game_params = GameParameters(maze_id, maze_img, maze_width, maze_height, algorithm)
game = Game(game_params)
game.bfs()

