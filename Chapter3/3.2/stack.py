class Stack:
    def __init__(self):
        self.items = []
        self.minn = None
        self.maxx = None
        self.size = 0
    def push(self, item):
    	if self.size == 0:
    		self.minn = item
    		self.maxx = item
    	if self.minn > item:
    		self.minn = item
        if self.maxx < item:
        	self.maxx = item
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    def get_max(self):
    	return self.maxx
    def get_min(self):
    	return self.min