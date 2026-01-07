import util

def easy_spawn(function):
	while max_drones()-num_drones()==0:
		do_a_flip()
	spawn_drone(function)
		
def pause():
	while num_drones()!=1:
		do_a_flip()