# You need to get the min and max number in a list.

# Your answer should be returned in an array containing the min and max number, respectively, as follows [min, max]

# In cases where the min and max numbers are equal, return an array with just the number, as the first index [number]

# Here are some examples

# [1, 2, 3] should return [1, 3]

# [1, 0, 8, 3] should return [0, 8]

# [-1, -55, -2] should return [-55, -1]

# [1, 1, 1] should return [1]


def findMaxMin(array):
	"""Mother function"""
	ans = [find_min(array), find_max(array)]
	
	# In cases where the min and max numbers are equal, return an array with just the number, as the first index [number]
	if ans[0] == ans[-1]:
		return [ans[0]]

	return ans


def find_min(array):
	"""Takes a list and return the smallest number in the list"""
	min_num = array[0]

	for num in array[1:]:
		if num < min_num:
			min_num = num

	return min_num


def find_max(array):
	"""Takes a list and returns the largest number"""
	max_num = array[0]

	for num in array[1:]:
		if num > max_num:
			max_num = num

	return max_num
