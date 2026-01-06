till_list=[Entities.Carrot,Entities.Pumpkin]
water_list=[Entities.Pumpkin]
fert_list=[Entities.Bush,Entities.Pumpkin]

def easy_plant(plant_type):
	if plant_type in till_list and get_ground_type()!= Grounds.Soil:
			till()
	plant(plant_type)
	if plant_type in fert_list:
		use_item(Items.Fertilizer)
	if plant_type in water_list:
		use_item(Items.Water)

def easy_harvest(plant_type):
	if can_harvest():
		harvest()
		easy_plant(plant_type)
	elif (not get_entity_type()) or get_entity_type()==Entities.Dead_Pumpkin:
		easy_plant(plant_type)
		
def easy_move(x,y):
	e=x-get_pos_x()
	n=y-get_pos_y()
	if e>0:
		for _ in range(e):
			move(East)
	else:
		for _ in range(abs(e)):
			move(West)
	if n>0:
		for i in range(n):
			move(North)
	else:
		for i in range(abs(n)):
			move(South)

def random_elem(list):
	index = random() * len(list) // 1
	return list[index]