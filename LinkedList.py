
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, data):
		self.data = data

	def set_next(self, next):
		self.next = next

class LinkedList:
	def __init__(self):
		self.top = None

	def append(self, data):
		if not self.top:
			self.top = Node(data)
		else:
			node = self.top
			while node.next:
				node = node.next
			added_node = Node(data)
			added_node.next = None
			node.next = added_node

	def show(self):
		node = self.top
		while node:
			print node.get_data(),
			node = node.next
		print

	def delete(self, n):
		if n == 0:
			if self.top:
				self.top = self.top.next
				return True
		else:
			node = self.top
			while node.next:
				n -= 1
				if n == 0:
					node.set_next(node.next.next)
					return True
				node = node.next
		return False

	def delete_dupricate(self):
		node1 = self.top
		if not node1:
			return False
		else:
			node2 = self.top
			while node1:
				node2 = node1
				while node2.next:
					if node1.data == node2.next.data :
						node2.next = node2.next.next
					else:
						node2 = node2.next

				node1 = node1.next


L = LinkedList()
L.append(0)
L.append(1)
L.append(2)
L.append(2)
L.append(1)
L.append(3)
L.append(3)

L.show()
L.delete_dupricate()
L.show()

