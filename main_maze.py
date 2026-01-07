import generate
import maze
import util
import control
import method

while num_items(Items.Gold)<=512000:
	if num_items(Items.Power)==0:
		method.easy_multi(method.mass_sunflower)
		
	else:
		generate.generate_maze(get_world_size())
		maze.clear_table()
		while max_drones()-num_drones()>0:
			control.easy_spawn(maze.rec_interface)
			if get_entity_type()!=Entities.Hedge:
				break
	control.pause()
