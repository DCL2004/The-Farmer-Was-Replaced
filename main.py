import util
import method
import control

CURRENT_JOB=None

def select_job1():
	if num_items(Items.Hay)<=20000 or num_items(Items.Wood)<=20000:
		return method.grass_tree
	elif num_items(Items.Carrot)<=5000:
		return method.mass_carrot
	else:
		return method.mass_pumpkin

def select_job2():
	if num_items(Items.Hay)<=20000 or num_items(Items.Wood)<=20000:
		return method.grass_tree
	elif num_items(Items.Carrot)<=5000:
		return method.mass_carrot
	else:
		return method.mass_sunflower
	
while True:
	job=select_job1()
	print(job)
	method.easy_multi(job)