def generate_maze(size):
	if get_entity_type()!=Entities.Hedge and can_harvest():
		harvest()
	plant(Entities.Bush)
	substance = size* 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
