from modules.settings import GameParameters
from modules.game import Game

game_params = GameParameters(
    'data/mazes/0.txt',
    'dfs',
    '',
    1, .01
)

game = Game(game_params)
path = game.solve()
print(game)

print('>> Path')
for coor in path:
    print(coor.get())