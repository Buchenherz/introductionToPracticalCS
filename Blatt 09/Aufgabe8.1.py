def log_two(k):
	if k > 0:
		return ((-1)**(k+1))/k + log_two(k - 1)
	else:
		return 0
	
# ln(2) = 0.6931471805...

print(log_two(997)) # prints 0.6936484335668373