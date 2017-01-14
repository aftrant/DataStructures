class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, data):
		if self.value == data:
			return False
		elif self.value > data:
			if self.left:
				return self.left.insert(data)
			else:
				self.left = Node(data)
				return True
		else:
			if self.right:
				return self.right.insert(data)
			else:
				self.right = Node(data)
				return True

	def find(self, data):
		if self.value == data:
			return True
		elif self.value > data:
			if self.left:
				return self.left.find(data)
			else:
				return False
		else:
			if self.right:
				return self.right.find(data)
			else:
				return False


	def preorder(self):
		if self:
			print str(self.value)
			if self.left:
				self.left.preorder()
			if self.right:
				self.right.preorder()

	def inorder(self):
		if self:
			if self.left:
				self.left.inorder()
			print str(self.value)
			if self.right:
				self.right.inorder()

	def postorder(self):
		if self:
			if self.left:
				self.left.postorder()
			if self.right:
				self.right.postorder()
			print str(self.value)

class Tree(object):
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True

	def find(self, data):
		if self.root:
			return self.root.find(data)
		else:
			return False

	def remove(self, data):
		if self.root is None:
			return False

		elif self.root.value == data:
			if self.root.left is None and self.root.right is None:
				self.root = None
		elif self.root.left and self.root.right is None:
			self.root = self.root.left
		elif self.root.right and self.root.left is None:
			self.root = self.root.right
		elif self.root.left and self.root.right:
			swapNodeParent = self.root
			swapNode = self.root.right
			while swapNode.left:
				swapNodeParent = self.root
				swapNode = self.root.left

			self.root.value = swapNode.value

			if swapNode.right:
				if swapNodeParent.value > swapNode.value:
					swapNodeParent.left = swapNode.right
				elif swapNodeParent.value < swapNode.value:
					swapNodeParent.right = swapNode.right
				else:
					if swapNode.value < swapNodeParent.value:
						swapNodeParent.left = None
					else:
						swapNodeParent.right = None

			return True



	def preorder(self):
		self.root.preorder()

	def inorder(self):
		self.root.inorder()

	def postorder(self):
		self.root.postorder()



bst = Tree()
bst.insert(10)
bst.insert(15)

bst.preorder()
bst.inorder()
bst.postorder()
