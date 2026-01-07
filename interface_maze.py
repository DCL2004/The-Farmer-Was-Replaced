import generate
import maze
import util

def maze_inter(num):
	while num_items(Items.Gold)<=num:
		generate.generate_maze(5)
		maze.clear_table()
		maze.rec(None)

spawn_drone(maze_inter(5000))
