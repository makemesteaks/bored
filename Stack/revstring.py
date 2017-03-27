import Stack

def revstring(mystr):
	myStack = Stack.Stack()
	return "".join([i for i in reversed(mystr)])

print revstring('ahah')