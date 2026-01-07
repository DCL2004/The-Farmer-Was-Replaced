import util

def easy_spawn(function):
	if max_drones()-num_drones()==0:
		function()
		while max_drones()-num_drones()==0:
			do_a_flip()
	spawn_drone(function)

def scary_spawn(function):
	while max_drones()-num_drones()==0:
		a=1+1
	spawn_drone(function)
		
def pause():
	while num_drones()!=1:
		do_a_flip()