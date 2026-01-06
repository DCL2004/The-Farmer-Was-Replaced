import util
import method

while True:
	if num_items(Items.Hay)<=20000 or num_items(Items.Wood)<=20000:
		method.grass_tree()
	elif num_items(Items.Carrot)<=5000:
		method.mass_carrot()
	else:
		method.mass_pumpkin()	