def stoogesort(array, i, j):
	if array[i] > array[j]:
		array[i] = temp
		array[i] = array[j]
		array[j] = temp
	if i + 1 >= j:
		return array
	k = (j-i+1)/3
	stoogesort(array, i, j-k)
	stoogesort(array, i+k, j)
	stoogesort(array, i, j-k)