def merge(l):
	n = len(l)
	if n > 1:
		half = n // 2
		left_list = l[:half]
		right_list = l[half:]
		
		merge(left_list)
		merge(right_list)
		index_list = index_left = index_right = 0
	
		while index_left < len(left_list) and index_right < len(right_list):
			if left_list[index_left] < right_list[index_right]:
				l[index_list] = left_list[index_left]
				index_left += 1
			else:
				l[index_list] = right_list[index_right]
				index_right += 1
			index_list += 1
			
		while index_left < len(left_list):
				l[index_list] = left_list[index_left]
				index_left += 1
				index_list += 1
			
		while index_right < len(right_list):
				l[index_list] = right_list[index_right]
				index_right += 1
				index_list += 1
			


if __name__ == "__main__":
	l = [17, 2, 89, 34, 123, 76, 13, 9, 56, 23, 18, 19, 11, 7, 12, 889, 11000, 234, 76, 45, 1, 345]
	
	print("Not sorted :",l)
	merge(l)
	print("Sorted :",l)
	