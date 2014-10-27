
class Cell:
	def __init__(self, x, y=None):
		self.data = x
		self.next = y

	def get_data(self, x):
		return self.data

	def get_next(self, x):
		return self.next

	def set_data(self, x):
		self.data = x

	def set_next(self, x):
		self.next = x