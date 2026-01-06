import generate
import maze

while num_items(Items.Gold)<=5000:
	generate.generate_maze()
	maze.clear_table()
	maze.rec(None)