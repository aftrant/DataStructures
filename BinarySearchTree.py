class Node(object):
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

	def getValue(self):
		return self.value

	def getLeftChild(self):
		return self.left

	def getRightChild(self):
		return self.right

	def setValue(self, v):
		self.value = v

	def setLeftChild(self, l):
		self.left = l

	def setRightChild(self, r):
		self.right = r


class BinarySearchTree(object):
	def __init__(self, root=None):
		self.head = None

	def insert(self, value):
		self._insert(self.head, value) 

	def _insert(self, root, value):
		if self.head == None:
			self.head = Node(value)
		elif value < root.value:
			if root.left:
				self._insert(root.left, value)
			else:
				root.left = Node(value)
		else:
			if root.right:
				self._insert(root.right, value)
			else:
				root.right = Node(value)
		return root

	def search(self, value):
		return self._search(self.head, value)

	def _search(self, node, find_value):
		if node:
			if find_value == node.value:
				return True
			elif find_value < node.value:
				if node.left:
					return self._search(node.left, find_value)
			else:
				if node.right:
					return self._search(node.right, find_value)
		return False

	def delete(self, value):
		return self._delete(self.head, value)

	def _delete(self, node, del_value):
		if node == None:
			return node
		elif del_value < node.value:
			node.left = self._delete(node.left, del_value)
		elif del_value < node.value:
			node.right = self._delete(node.right, del_value)
		else:	
			if node.left is None and node.right is None:
				node = None
			elif node.left is None:
				tmp_node = node
				node = node.right
			elif node.right is None:
				tmp_node = node
				node = node.left
			else:
				min_node = self.find_min(node.right)
				node.data = min_node.data
				node.right = self._delete(node.right, min_node.data)
		return node

	def find_min(self, node):
		current_node = node
		while current_node.left:
			current_node = current_node.left
		return current_node

	def height(self):
		return self._height(self.head)

	def _height(self, node):
		if node is None:
			return -1
		
		left_height = self._height(node.left)
		right_height = self._height(node.right)

		return max(left_height, right_height) + 1

def preorder(root):
	if not root:
		return
	print root.value
	preorder(root.left)
	preorder(root.right)

def inorder(root):
	if not root:
		return
	inorder(root.left)
	print root.value
	inorder(root.right)

def postorder(root):
	if not root:
		return
	postorder(root.left)
	postorder(root.right)
	print root.value

binaryTree = BinarySearchTree()
binaryTree.insert(5)
binaryTree.insert(10)
binaryTree.insert(2)
binaryTree.insert(1)
binaryTree.insert(6)
binaryTree.insert(15)

print preorder(binaryTree.head)

print binaryTree.search(2)
print binaryTree.search(15)
print binaryTree.search(3)

print preorder(binaryTree.head)
binaryTree.delete(2)
print preorder(binaryTree.head)

print binaryTree.height()
