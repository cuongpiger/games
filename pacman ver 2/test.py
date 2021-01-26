from modules.settings import GameParameters
from modules.game import Game

game_params = GameParameters(
    'data/mazes/0.txt',
    'bfs',
    'Manhattan',
    1, .3
)

game = Game(game_params)
print(game)
