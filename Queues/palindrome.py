import Deque


def palindrome(string):
	d = Deque.Deque()

	for i in string:
		d.addFront(i)

	while d.size() > 1:
		first = d.removeRear()
		last = d.removeFront()

		if first != last:
			return "{} isn't a palindrome!".format(string)
	return "{} is a palindrome!".format(string)


print palindrome("ababababababaaaaaa")