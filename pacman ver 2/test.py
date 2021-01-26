from modules.settings import GameParameters
from modules.game import Game

game_params = GameParameters(
    'data/mazes/1.txt',
    'bfs',
    '',
    1, .7
)

game = Game(game_params)
game.solve()
print(game)