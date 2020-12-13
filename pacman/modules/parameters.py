class GameParameters:
    def __init__(self, maze, maze_width, maze_height):
        self.maze = maze # path to current maze
        self.maze_width = maze_width
        self.maze_height = maze_height

    def update(self, maze, maze_width, maze_height):
        self.maze = maze
        self.maze_width = maze_width
        self.maze_height = maze_height