class Node(object):
	def __init__(self, data, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def get_prev(self):
		return self.prev

	def set_next(self, n):
		self.next = n

	def set_prev(self, n):
		self.prev = n

def LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def insert(self, data):
		new_node = Node(data)
		current_node = self.head
		next_node = current_node.get_next()

		while next_node:
			current_node = current_node.get_next()

		current_node.set_next(n)
		new_node.set_prev(current_node)
	
	def delete(self, data):
		current_node = self.head
		prev_node = current_node.get_prev()
		next_node = current_node.get_next()

		found = False

		while current_node and found is False:
			if current_node.get_data() == data:
				found = True
			else:
				current_node = current_node.get_next()

		if prev_node is None:
			self.head = next_node

		if next_node is None:
			raise ValueError('data not in list')
		else:
			previous_node.set_next(next_node)
			next_node.set_prev(previous_node)
