class GameParameters:
    def __init__(self, maze, maze_width, maze_height, algorithm):
        self.maze = maze # path to current maze
        self.maze_width = maze_width
        self.maze_height = maze_height
        self.algorithm = algorithm
        self.feed_density = .0
        self.pacman_speed = 1

    def update_maze(self, maze, maze_width, maze_height):
        self.maze = maze
        self.maze_width = maze_width
        self.maze_height = maze_height