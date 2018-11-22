class Node:
	def __init__(self,data = None):
		self.d = data
		self.l = None
		self.r = None
	def getDat(self):
		return self.d
	def add(self,aNode):
		if self.d == None:
			self.d = aNode.getDat()
			return
			
		if self.d > aNode.getDat():
			self.l.add(aNode)
		else:
			self.r.add(aNode)