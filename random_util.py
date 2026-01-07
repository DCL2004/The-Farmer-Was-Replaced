def random_element(list):
	index = random() * len(list) // 1
	return list[index]

def shuffle(list):
	for i in range(len(list)-1,0,-1):
		j=random()*(i+1)//1
		list[i],list[j]=list[j],list[i]
	return list