
class Cell:
	def __init__(self,x,y=None):
		self.data = x
		self.next = y

	def first(self):
		return self.data

	def rest(self):
		return self.next

	def set_first(self,x):
		self.data=x

	def set_rest(self,x):
		self.next=x

class LinkedList:
	def __init__(self):
		self.top = None

	def insert(self, n, x):
		if n == 0 or not self.top:
			self.top = Cell(x, self.top)
		else:
			cp = self.top
			while cp.rest():
				n -= 1
				if n == 0: 
					break
				cp = cp.rest()
			new_cp = Cell(x, cp.rest())
			cp.set_rest(new_cp)

	def delete(self, n):
		if n == 0:
			if self.top:
				self.top = self.top.rest()
				return True
		else:
			cp = self.top
			while cp.rest():
				n -= 1
				if n == 0:
					cp.set_rest(cp.rest().rest())
					return True
				cp = cp.rest()
		return False


	def index(self, x):
		n = 0
		cp = self.top
		while cp:
			if cp.first() == x: return n
			n += 1
			cp = cp.rest()
		return -1

L = LinkedList()
L.insert(3, 2)
L.insert(2, 3)
print L.index(3)
print "aaa"
