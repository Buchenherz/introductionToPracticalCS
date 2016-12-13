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
        i.next = i.next.next  # zeigt auf "übernächsten wert", da "nächste" Wert der neue Wert ist.
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

### End Stack ###

print("\n --- \n")

### Queue ###
def init_q():
    return None

def isEmpty_q(list):
    return list is None

def isFull_q(list):
    return False

def get(list):
    return delete(list.data, list)

def front(list):
    return list.data

### End Cueue ###

def QueueInit():
    global INBOX, OUTBOX
    INBOX = init_s()
    OUTBOX = init_s()

def isOutboxEmpty():
    return not OUTBOX

def isInboxEmpty():
    return not INBOX

def put(value):
    append(value, INBOX)
    return True

def pop():
    if(isOutboxEmpty()):
        if(isInboxEmpty()):
            return False
        for i in range(len(INBOX)):
            OUTBOX = OUTBOX.append(INBOX[-1])
            del INBOX[-1]
        return pop()
    element = OUTBOX[-1]
    del OUTBOX[-1]
    return element

QueueInit()
put(1)
put(10)
put("a")
put("b")
print("Inbox: ", INBOX)
print("Outbox: ", OUTBOX)
print("Front: ", pop())
put("c")
put(100)
print("Inbox: ", INBOX)
print("Outbox: ", OUTBOX)
print("Front again: ", pop())
put(":^}")
print("Front once again: ", pop())
print("Once more: ", pop())
print("Once more: ", pop())
print("Just one more time: ", pop())
print("Last one, promise: ", pop())
print("Well, I had to insert one more, to test, what happens when both stacks are empty: ", Pop())
