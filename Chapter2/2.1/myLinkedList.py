'''
a simply implemented linked List
@author: Anh Nguyen (not stackoverflow at all)
'''
class myLinkedList:
	def __init__(self,d= None):
		self.d = d
		self.n = None
	def addEnd(self,d):
		tmp = myLinkedList(d)
		ite = self
		while(self.n != None):
			self = self.n
		self.n = tmp
	def delete(self,d):
		if self.d == d:
			return self.n
		h = self
		while self.n != None:
			if self.n.d == d:
				self.n = self.n.n
				return h
			self = self.n
		return h
	def toString(self):
		if self.n == None:
			return str(self.d)
		ans = str(self.d)
		while self.n != None:
			self = self.n
			ans +='->'+str(self.d) 
			
		return ans

def testMyLinkedList():
	print("Creation")
	l = myLinkedList(5)
	print(l.toString())
	print("add end 4")
	l.addEnd(4)
	print(l.toString())
	print("add end 5")
	l.addEnd(5)
	print(l.toString())
	print("add end 6")
	l.addEnd(6)
	print(l.toString())
	print("delete 5")
	l = l.delete(5)
	print(l.toString())
	print("delete 5")
	l = l.delete(5)
	print(l.toString())
	print("add end 3")
	l.addEnd(3)
	print(l.toString())
	print("add end 2")
	l.addEnd(2)
	print(l.toString())
	print("add end 1")
	l.addEnd(1)
	print(l.toString())
	print("delete 6")
	l = l.delete(6)
	print(l.toString())
	print("delete 1")
	l = l.delete(1)
	print(l.toString())


if __name__ == '__main__':
	testMyLinkedList()
