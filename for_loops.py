# for item in range(1,21):
# 	print item,

# for item in range(1,21):
# 	if item == 13:
# 		print "hello"
# 	else: 
# 		print item,

fruits_list = ["apples", "oranges", "bananas"]	
for item in fruits_list:
	print item, 

# fruits_list = ["apples", "oranges", "bananas"]	
# for item in range(len(fruits_list)):
# 	print type(item)
# 	print fruits_list[item]


def sum_nums(num):
	my_list = range(num)
	return sum(my_list)
	
print sum_nums(10)