class Stack:
	def __init__(self):
		self.s = []
		self.size = 0
	def add(self,item):
		self.size +=1
		self.s.append(item)
	def pop(self):
		if self.empty():
			return None
		self.size -= 1
		return self.s.pop()
	def empty(self):
		return self.size == 0
	def toString(self):
		return str(self.s)
class SetOfStack:
	def __init__(self,threashold):
		self.t = threashold
		cur = Stack()
		self.setOfStack = [cur]
	def add(self,item):
		if self.setOfStack[-1].size >= self.t:
			cur = Stack()
			cur.add(item)
			self.setOfStack.append(cur)
		else:
			self.setOfStack[-1].add(item)
	def pop(self):
		if len(self.setOfStack) == 0:
			return "it's empty bro"
		if self.setOfStack[-1].empty():
			self.setOfStack.pop()
		return self.setOfStack[-1].pop()
	def toString(self):
		ans = '['
		for i in range(len(self.setOfStack)):
			ans += self.setOfStack[i].toString()
		return ans + ']'


