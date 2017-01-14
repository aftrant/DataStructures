class Node(object):
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, n):
		self.next = n

	def __str__(self):
		return str(self.data)


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def insert(self, data):
		new_node = Node(data)
		new_node.set_next = self.head
		self.head = new_node

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count

	def search(self, data):
		current_node = self.head
		found = False
		while current_node and found is False:
			if current_node.get_data() == data:
				found = True
			else:
				current_node = current_node.get_next()
		if current_node is None:
			raise ValueError("Data not in list")
		return current_node

	def delete(self, data):
		current_node = self.head
		previous_node = None
		found = False
		while current_node and found is False:
			if current_node.get_data() == data:
				found = True
			else:
				previous_node = current_node
				current_node = current_node.get_next()

		if current_node is None:
			raise ValueError("Data not in list")
		if previous_node is None:
			self.head = current_node.get_next()
		else:
			previous_node.set_next(current_node.get_next)
