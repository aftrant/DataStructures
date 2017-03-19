class Node(object):
	def __init__(self, data, left=None, right=None, parent=None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent

class BinarySearchTree(object):
	def __init__(self, root=None):
		self.head = None

	def insert(self, data):
		self._insert(self.head, data) 

	def _insert(self, root, data):
		if self.head == None:
			self.head = Node(data)
		elif data < root.data:
			if root.left:
				self._insert(root.left, data)
			else:
				root.left = Node(data)
		else:
			if root.right:
				self._insert(root.right, data)
			else:
				root.right = Node(data)
		return root

	def search(self, data):
		return self._search(self.head, data)

	def _search(self, node, find_data):
		if node:
			if find_data == node.data:
				return True
			elif find_data < node.data:
				if node.left:
					return self._search(node.left, find_data)
			else:
				if node.right:
					return self._search(node.right, find_data)
		return False

	def delete(self, data):
		return self._delete(self.head, data)

	def _delete(self, node, del_data):
		if node == None:
			return node
		elif del_data < node.data:
			node.left = self._delete(node.left, del_data)
		elif del_data < node.data:
			node.right = self._delete(node.right, del_data)
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
	print root.data
	preorder(root.left)
	preorder(root.right)

def inorder(root):
	if not root:
		return
	inorder(root.left)
	print root.data
	inorder(root.right)

def postorder(root):
	if not root:
		return
	postorder(root.left)
	postorder(root.right)
	print root.data

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
