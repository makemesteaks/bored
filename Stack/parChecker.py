import Stack

def parChecker(symbol):
	s=Stack.Stack()
	Balanced=True
	index=0
	while index < len(symbol) and Balanced:
		sy = symbol[index]
		if sy == "(":
			s.push(sy)
		else:
			if s.isEmpty():
				Balanced = False
			else:
				s.pop()
		index+=1

	if Balanced and s.isEmpty():
		return True
	else:
		return False

print(parChecker('((()))'))
print(parChecker('(()'))
