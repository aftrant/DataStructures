class node(object):
	def __init__(self, name, parent=-1):
		self.name = name
		self.parent = parent
		self.children = []

	def getName(self):
		return self.name

	def getParent(self):
		return self.parent

	def getChildren(self):
		return self.children

	def setParent(self, p):
		self.parent = p

	def addChild(self, c):
		self.children.append(c)


