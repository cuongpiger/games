'''Demo write json file'''
""" from modules.ultility_functions import write_json_file

data = [
    {
        'title': 'Maze 0',
        'path': r'data/images/mazes/maze_0.png'
    },
    {
        'title': 'Maze 0',
        'path': r'data/images/mazes/maze_0.png'
    }
]


write_json_file(r'data/text/maze_info.json', data) """

################################################################################################

'''Demo read json file'''
""" from modules.ultility_functions import read_json_file

data = read_json_file(r'data/text/maze_info.json')

print(data) """

################################################################################################
'''Demo lambda'''
algos = [{"title": "Breadth First Search", "name": "bfs"}, {"title": "Depth First Search", "name": "dfs"}]

# index = algos.index(filter(lambda item: item.get('name') == 'bfs', algos)[0])

tmp = list(filter(lambda item: item.get('name') == 'bfs', algos))

print(tmp)