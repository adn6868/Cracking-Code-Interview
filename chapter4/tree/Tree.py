class Tree:
	def __init__ (self, data = None):
		self.d = data
		self.children =[]
		self.size =0
	def addChild(self,aNode):
		self.children.append(aNode)
	def removeChild(self,aNode):
		self.children.remove(aNode)
	def getSize(self):
		return self.size

	def toString(self):
		if self == None:
			return ""
		ans = ""
		ans = ans + "[" +str(self.d)
		for child in self.children:
			ans += child.toString()+","
		return ans + "]"
