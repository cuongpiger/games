from modules.parameters import GameParameters
from modules.game import Game

maze_id, maze_img, maze_width, maze_height, algorithm = 1, 'data/images/mazes/maze_0.png', 840, 930, 'bfs'

game_params = GameParameters(maze_id, maze_img, maze_width, maze_height, algorithm)
game = Game(game_params)


game.print_board()
print(game.pacman_pos)
