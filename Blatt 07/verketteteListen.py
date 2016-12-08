# We initialise the first element of the list

class Node:
	def __init__(self, d):
		# d is the first element
		self.data = d       
		# element after is None
		self.next = None    

### Add element at beginning of list ###
def prepend(data, list):    
	# First element of list get's changed to value of data
	node = Node(data)       
	# The previous element is placed on the second element
	node.next = list       
	return node

### Add element at end of list ###
def append(data, list):
	node = Node(data)
	# if list is none, set next element to none and return
	# new value
	if list is None:        
		node.next = None    
		return node
	# Create helper var i to not lose the value of list
	# If list is lost, we won't be able to find our data
	i = list
	while i.next is not None:
		# go to the next element in list
		i = i.next          
	# when next element is none, set the element to new value
	# and the next to none
	i.next = node
	node.next = None
	return list

### Delete element from list ###
def delete(data, list):     
	# if the list is none, there's nothing to be deleted
	if list is None:        
		return None         
	# if the first item of list is our wanted item, 
	# return list.next, to set the start of the list to the next element.
	if list.data is data:   
		return list.next
	# Same as before
	i = list
	# Search for wanted item
	while i.next is not None and i.next.data is not data:
		i = i.next
	if i.next is not None:
	# FIXME i have no clue
		i.next = i.next.next        #zeigt auf "übernächsten wert", da "nächste" Wert der neue Wert ist.
	return list



### Stack ###
def init_s():
	return None

def isEmpty_s(list):
	return list is None

def isFull_s(list):
	return False

def push(data, list):
	return prepend(data, list)

def pop(list):
	return delete(list.data, list)

def top(list):
	return list.data

def popTop(list):
	w = top(list)
	pop(list)
	return w

ket_stack = init_s()
print(isEmpty_s(ket_stack))
ket_stack = push(10, ket_stack)
ket_stack = push(20, ket_stack)
ket_stack = pop(ket_stack)
print(top(ket_stack))

### End Stack ###

print("\n --- \n")

### Queue ###
def init_q():
	return None

def isEmpty_q(list):
	return list is None

def isFull_q(list):
	return False
	
def put(data, list):
	return append(data, list)

def get(list):
	return delete(list.data, list)

def front(list):
	return list.data
	
ket_queue = init_q()
ket_queue = put(21, ket_queue)
print(front(ket_queue))
ket_queue = get(ket_queue)
print(isEmpty_q(ket_queue))
ket_queue = put(21, ket_queue)
ket_queue = put(22, ket_queue)
ket_queue = get(ket_queue)
print(front(ket_queue))
### End Cueue ###

