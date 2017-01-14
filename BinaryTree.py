class Node(object):
	def __init__(self, data=None, parent=-1, left=None, right=None):
		self.data = data
		self.parent = parent
		self.left = left
		self.right = right

	def get_data(self):
		return self.data

	def get_parent(self):
		return self.parent

	def get_left(self):
		return self.left

	def get_right(self):
		return self.right

	def set_data(self, d):
		self.data = d

	def set_parent(self, p):
		self.parent = p

	def set_left(self, l):
		self.left = l

	def set_right(self, r):
		self.right = r

class BinaryTree(object):
	def __init__(self, root):
		self.key = root
		self.left = None
		self.right = None

	def insertLeft(self, node):
		if self.left == None:
			self.left = BinaryTree(node)
		else:
			t = BinaryTree(node)
			t.left = self.left
			self.left = t

	def insertRight(self, node):
		if self.right == None:
			self.right = BinaryTree(node)
		else:
			t = BinaryTree(node)
			t.right = self.right
			self.right = t

	def getRightChild(self):
		return self.right

	def getLeftChild(self):
		return self.left

	def setRootValue(self, root):
		self.key = root

	def getRootValue(self):
		return self.key


def insert(self, insert_node):
	if nodelist[insert_node].get_data() < self.data:
		if self.left == None:
			self.left = insert_node
		else:
			nodelist[self.left].insert(insert_node)
	else:
		if self.right == None:
			self.right = insert_node
		else:
			nodelist[self.right].insert(insert_node)

