import util
import random_util
import control

def pumpkin_check():
	if not measure():
		return False
	value=measure()
	for _ in range(get_world_size()):
		if value!=measure():
			return False
		value=measure()
		move(North)
	if value!=measure():
		return False
	return True

def pumpkin_rec():
	if not measure() or measure()<10000:
		util.easy_harvest(Entities.Pumpkin)
		return True
	for dir in [North,East,South,West]:
		if not measure(dir) or measure(dir)<10000:
			move(dir)
			return pumpkin_rec()
	return False

def mass_pumpkin():
	while not pumpkin_check():
		move(random_util.random_element([East,East,East,East,North,South,West]))
		pumpkin_rec()
	harvest()

def mass_carrot():
	for _ in range(get_world_size()):
		util.easy_harvest(Entities.Carrot)
		move(North)
	move(East)

def grass_tree():
	for _ in range(get_world_size()):
		if (get_pos_x()+get_pos_y())%4==0:
			util.easy_harvest(Entities.Tree)
		else:
			util.easy_harvest(Entities.Grass)
		move(North)
	move(East)

def mass_sunflower():
	for _ in range(get_world_size()):
		util.easy_harvest(Entities.Sunflower)
		move(North)
	
def mass_cactus():
	for _ in range(get_world_size()):
		cnt=1
		while cnt!=0:
			cnt=0
			for _ in range(get_world_size()):
				if get_entity_type()!=Entities.Cactus:
					util.easy_plant(Entities.Cactus)
					cnt+=1
				elif get_pos_y()<get_world_size()-1 and measure(North)<measure():
					swap(North)
					cnt+=1
				move(North)
		move(East)
	for _ in range(get_world_size()):
		cnt=1
		while cnt!=0:
			cnt=0
			for _ in range(get_world_size()):
				if get_entity_type()!=Entities.Cactus:
					util.easy_plant(Entities.Cactus)
					cnt+=1
				elif get_pos_x()<get_world_size()-1 and measure(East)<measure():
					swap(East)
					cnt+=1
				move(East)
		move(North)
	harvest()

def naive_dinasaur_iter():
	clear()
	change_hat(Hats.Dinosaur_Hat)
	flag=True
	while flag:
		move(North)
		for i in range(get_world_size()):
			for j in range(get_world_size()-2):
				if i%2==0:
					move(North)
				else:
					move(South)
			move(East)
		move(South)
		util.easy_move(0,0)
		flag=can_move(North) or can_move(East) or can_move(South) or can_move(West)
	clear()

def sort_cactus(dir):
	def dir_func(dir):
		if dir==East or dir==West:
			return get_pos_x() 
		else:
			return get_pos_y()
	cnt=1
	while cnt!=0:
		cnt=0
		for _ in range(get_world_size()):
			if get_entity_type()!=Entities.Cactus:
				util.easy_plant(Entities.Cactus)
				cnt+=1
			elif dir_func(dir)<get_world_size()-1 and measure(dir)<measure():
				swap(dir)
				cnt+=1
			move(dir)

def multi_cactus():
	def sort_north():
		sort_cactus(North)
	def sort_east():
		sort_cactus(East)
	for _ in range(get_world_size()):
		control.easy_spawn(sort_north)
		move(East)
	control.pause()
	for _ in range(get_world_size()):
		control.easy_spawn(sort_east)
		move(North)
	control.pause()
	harvest() 

def easy_multi(function):
	while max_drones()-num_drones()>0:
		control.easy_spawn(function)
		move(East)
	control.pause()
		