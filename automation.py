import method

map={Items.Hay:Entities.Grass,Items.Wood:Entities.Tree,Items.Carrot:Entities.Carrot,Items.Pumpkin:Entities.Pumpkin,Items.Cactus:Entities.Cactus,Items.Power:Entities.Sunflower}

def item_selection(item):
	if item in map:
		select_target(get_cost(map[item]))
	if item==Items.Power:
		method.multi_sunflower()
	elif item==Items.Hay or Items==Items.Wood:
		method.multi_grass_tree()
	elif item==Items.Carrot:
		method.multi_carrot()
	elif item==Items.Pumpkin:
		method.multi_pumpkin()
	elif item==Items.Cactus:
		method.multi_cactus()
	return None

def select_target(target):
	for item in target:
		while num_items(item)<target[item]:
			item_selection(item)

def run_on_time(time,function):
	time1=get_time()
	time2=get_time()
	while time2-time1<time:
		function()
			