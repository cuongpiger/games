class GameParameters:
    def __init__(self, maze_id, maze_img, maze_width, maze_height, algorithm):
        self.maze_id = maze_id
        self.maze_img = maze_img # path to current maze
        self.maze_width = maze_width
        self.maze_height = maze_height
        self.algorithm = algorithm
        self.feed_density = .1
        self.pacman_speed = 1

    def update_maze(self, maze_id, maze_img, maze_width, maze_height):
        self.maze_id = maze_id
        self.maze_img = maze_img
        self.maze_width = maze_width
        self.maze_height = maze_height