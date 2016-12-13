def binary_search(E,A,I,J):
	if ((I == J) and (E != A[I])):
		return -1
	elif E is A[int((I+J)/2)]:
		return (I+J)/2
	elif E < A[int((I+J)/2)]:
		return binary_search(E, A, I, (int((I+J)/2)-1))
	elif E > A[int((I+J)/2)]:
		I = int((I+J)/2)+1
		return binary_search(E, A, I, J)
	
A = [0,1,2,3,4,5,6,7,8,9]

print(binary_search(1, A, 1, 1))

