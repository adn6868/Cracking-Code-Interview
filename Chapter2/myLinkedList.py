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
