my_list = ["apples", "bananas", "kiwi"]

def add_shopping(add_item):
	if add_item.lower() in my_list: 
		print "Already exists!"
	else:
		my_list.append(add_item)
	my_list.sort()
	return my_list


def main(): 
	add = raw_input("What would you like to add to your grocery list?")

	print add_shopping(add)

if __name__ == '__main__':
	main()