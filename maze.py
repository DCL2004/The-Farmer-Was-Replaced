import random_util

map={North:South,East:West,South:North,West:East}
table={}

def rec(last_step,dir_order):
	if get_entity_type()!=Entities.Hedge:
		harvest()
		return True
	pos=(get_pos_x(),get_pos_y())
	if pos not in table:
		table[pos]=set()
	if last_step:
		table[pos].add(last_step)
	for dir in dir_order:
		if dir in table[pos] or not can_move(dir):
			continue
		table[pos].add(dir)
		move(dir)
		if rec(map[dir],dir_order):
			return True
		move(map[dir])
	return False

def clear_table():
	global table
	table={}

def print_table():
	print(table)

def rec_interface():
	dir_order=random_util.shuffle([North,East,South,West])
	rec(None,dir_order)