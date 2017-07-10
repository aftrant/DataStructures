class Stack():
	def __init__(self):
		self._stack = []
		self._min = None

	def push(self, item):
		self._stack.append(item)

	def pop(self):
		self._stack.pop()

	def peek(self):
		if self._stack:
			return self._stack(len(self._stack)-1)

	def isEmpty(self):
		return (len(self._stack) == 0)

	def setMin(self, n):
		self._min = n

	def min(self):
		return self._min

	def size(self):
		return len(self._stack)

	def getValue(self, x):
		return self._stack[x]

	def __getitem__(self, x):
		return self._stack[x]

	def getStack(self):
		return self._stack

class Node():
	def __init__(self, value):
		self._value = value

	def getValue(self):
		return self._value
	

s = Stack()
n = Node(3)
s.push(n)
n = Node(6)
s.push(n)
n = Node(2)
s.push(n)
n = Node(1)
s.push(n)
n = Node(9)
s.push(n)


#print s
#print s.getStack()

for index in range(s.size()):
	print 'current node value'
	print s[index].getValue()
	print 'Current min'
	print s.min()
	if s.min() == None:
		print 'Setting initial min'
		s.setMin(s[index].getValue())
	elif s[index].getValue() < s.min():
		print 'Setting new min'
		print s[index].getValue()
		s.setMin(s[index].getValue())

print s.min()
