A = [1,8,9,2,6,4,3,5,7] #unsorted array

# Variable i is used as starting value (0 in our case)
# j is the last value of the array (just len(array)-1
def stoogesort(A, i, j):
	if A[i] > A[j]:
		temp = A[i]
		A[i] = A[j]
		A[j] = temp
	# More than two items in array?
	if i+1 >= j:
		# No:
		return A
		
	# Yes:
	# A third of the array
	k = int((j-i+1)/3)
	
	stoogesort(A, i, j-k) # sort first two thirds
	stoogesort(A, i+k, j) # sort last two thirds
	stoogesort(A, i, j-k) # sort first two thirds
	
stoogesort(A, 0, len(A)-1)
print(A)
