import Stack

def divideBy(decNumber,base):
    remstack = Stack.Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divideBy(171,8))
print(divideBy(26,26))