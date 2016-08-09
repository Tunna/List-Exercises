my_list = ["apples", "bananas", "kiwi"]

def add_shopping(add_item):
	if add_item.lower() in my_list: 
		print "This item %s already exists!" % (add_item)
	else:
		my_list.append(add_item)
	my_list.sort()
	return my_list


def remove_shopping(delete_item):
	if delete_item.lower() not in my_list:
		print "This item %s not in list therefore cannot be removed." % (delete_item)
	else:
		my_list.remove(delete_item)
	my_list.sort()
	return my_list	


def menu_function():
	print "Please select one of the options below."
	print "0 - Main Menu"
	print "1 - Show current list."
	print "2 - Add an item to your shopping list."
	print "3 - Remove an item from shopping list."
	print "Type exit to exit."
	option = raw_input("Enter your selection: ")
	return option
	
def main(): 
	

	

	
	while (True):
		option = menu_function()
		if option == "exit":
			break
		elif option == "0":
			pass
		elif option == "1":
			print "Your items are", my_list
		elif option == "2":
			add = raw_input("What would you like to add to your grocery list?")
			print add_shopping(add)
		elif option == "3":
			remove = raw_input('What would you like to remove from your grocery list?')
			print remove_shopping(remove)
		else:
			print "Invalid option. Please try again."
			

if __name__ == '__main__':
    main()




