def binary_search(array, x:int, low, high) ->int:
	if low <= high:
		mid = low + (high - low) // 2
		if array[mid] == x:
			return mid
		elif x > array[mid]:
			return binary_search(array, x, mid+1, high)
		else:
			return binary_search(array, x, low, mid -1)
	else:
		return -1


if __name__ == "__main__":
	
	array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	
	result = binary_search(array, 7, 0, len(array)-1)
	
	if result != -1:
		print("Element found at index " + str(result))
	else:
		print("Element not Found!!")