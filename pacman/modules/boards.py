from modules.settings import GameSettings

gameSt = GameSettings()
w = gameSt.wall
p = gameSt.path

board_0 = [
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [w, p, p, p, p, p, p, p, p, p, p, p, p, w, w, p, p, p, p, p, p, p, p, p, p, p, p, w],
    [w, p, w, w, w, w, p, w, w, w, w, w, p, w, w, p, w, w, w, w, w, p, w, w, w, w, p, w],
    [w, p, w, w, w, w, p, w, w, w, w, w, p, w, w, p, w, w, w, w, w, p, w, w, w, w, p, w],
    [w, p, w, w, w, w, p, w, w, w, w, w, p, w, w, p, w, w, w, w, w, p, w, w, w, w, p, w],
    [w, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
    [w, p, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, p, w, w, w, w, p, w],
    [w, p, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, p, w, w, w, w, p, w],
    [w, p, p, p, p, p, p, w, w, p, p, p, p, w, w, p, p, p, p, w, w, p, p, p, p, p, p, w],
    [w, w, w, w, w, w, p, w, w, w, w, w, p, w, w, p, w, w, w, w, w, p, w, w, w, w, w, w],
    [w, w, w, w, w, w, p, w, w, w, w, w, p, w, w, p, w, w, w, w, w, p, w, w, w, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, p, p, p, p, p, p, p, p, p, w, w, p, w, w, w, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w],
    [w, w, w, w, w, w, p, p, p, p, w, w, w, w, w, w, w, w, p, p, p, p, w, w, w, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, p, p, p, p, p, p, p, p, p, w, w, p, w, w, w, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w],
    [w, p, p, p, p, p, p, p, p, p, p, p, p, w, w, p, p, p, p, p, p, p, p, p, p, p, p, w],
    [w, p, w, w, w, w, p, w, w, w, w, w, p, w, w, p, w, w, w, w, w, p, w, w, w, w, p, w],
    [w, p, w, w, w, w, p, w, w, w, w, w, p, w, w, p, w, w, w, w, w, p, w, w, w, w, p, w],
    [w, p, p, p, w, w, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, w, w, p, p, p, w],
    [w, w, w, p, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, p, w, w, p, w, w, w],
    [w, w, w, p, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, p, w, w, p, w, w, w],
    [w, p, p, p, p, p, p, w, w, p, p, p, p, w, w, p, p, p, p, w, w, p, p, p, p, p, p, w],
    [w, p, w, w, w, w, w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, w, w, p, w],
    [w, p, w, w, w, w, w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, w, w, p, w],
    [w, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
]


board_1 = [
    [w, w, w, w, w, w],
    [w, p, p, p, p, w],
    [w, w, p, w, p, w],
    [w, w, p, w, p, w],
    [w, w, w, w, w, w],
]

board_2 = [
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [w, p, p, p, p, p, p, p, p, p, p, p, p, w, w],
    [w, p, w, w, w, w, p, w, w, w, w, w, p, w, w],
    [w, p, w, w, w, w, p, w, w, w, w, w, p, w, w],
    [w, p, w, w, w, w, p, w, w, w, w, w, p, w, w],
    [w, p, p, p, p, p, p, p, p, p, p, p, p, p, p],
    [w, p, w, w, w, w, p, w, w, p, w, w, w, w, w],
    [w, p, w, w, w, w, p, w, w, p, w, w, w, w, w],
    [w, p, p, p, p, p, p, w, w, p, p, p, p, w, w],
    [w, w, w, w, w, w, p, w, w, w, w, w, p, w, w],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]
]


board_3 = [
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [w, p, p, p, p, p, p, p, p, p, p, p, p, w, w, p, p, p, p, p, p, w],
    [w, p, w, w, w, w, p, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w],
    [w, p, w, w, w, w, p, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w],
    [w, p, w, w, w, w, p, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w],
    [w, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
    [w, p, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, w],
    [w, p, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, w],
    [w, p, p, p, p, p, p, w, w, p, p, p, p, w, w, p, p, p, p, w, w, w],
    [w, w, w, w, w, w, p, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w],
    [w, w, w, w, w, w, p, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, p, p, p, p, p, p, p, p, p, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, w],
    [w, w, w, w, w, w, p, p, p, p, w, w, w, w, w, w, w, w, p, p, p, w],
    [w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, p, p, p, p, p, p, p, p, p, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, w],
    [w, w, w, w, w, w, p, w, w, p, w, w, w, w, w, w, w, w, p, w, w, w],
    [w, p, p, p, p, p, p, p, p, p, p, p, p, w, w, p, p, p, p, p, p, w],
]

boards = [board_0, board_1, board_2, board_3]
