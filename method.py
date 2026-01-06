import util

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
		harvest()
		util.easy_plant(Entities.Pumpkin)
	for dir in [North,East,South,West]:
		if not measure(dir) or measure(dir)<10000:
			move(dir)
			pumpkin_rec()

def mass_pumpkin():
	while not pumpkin_check():
		move(util.random_elem([East,East,East,East,North,South,West]))
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
	move(East)