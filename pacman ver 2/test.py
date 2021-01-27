from modules.settings import GameParameters
from modules.game import Game

game_params = GameParameters(
    'data/mazes/1.txt',
    'bfs',
    '',
    1, .01
)

game = Game(game_params)
path = game.solve()
print(game)

for coor in path:
    print(coor.get())