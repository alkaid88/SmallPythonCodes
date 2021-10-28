# Just a simple 2 functions that are using Pythagorean theorem to draw circle to the screen


# This function is for creating circle inside of a list
def Circle(r):
	list = []
	for i in range(-r, r+1, 1):
		for j in range(-r, r+1, 1):
			if j**2 + i**2 == r**2:
				list.append(1)
			else:
                            	list.append(0)
		list.append(2)
	return list

# This function uses list to determine what to print
def DrawCircle(r ,some_list):
	for x in range(0, 4*r**2+6*r+2, 1):
		if some_list[x] == 1:
			print('*', end='')
		elif some_list[x] == 0:
			print(' ', end='')
		elif some_list[x] == 2:
			print()
			
