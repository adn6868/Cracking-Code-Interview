import sys
import itertools
class Output:
	def __init__(self):
		self.o = sys.stdout
	def write( self, aline ):
		self.o.write(str(aline))
	def writeln(self, aline):
		self.o.write(str(aline) + '\n')

class Input:
	def __init__( self ):
		self.i = sys.stdin
	def readline( self ):
		return self.i.readline().strip('\n')
	def readInt( self ):
		return int ( self.i.readline().strip('\n'))
	def readFlt( self ):
		return float(self.i.readline().strip('\n'))
	def readToList(self,splitter = " "):
		return list(self.i.readline().strip('\n').split(splitter))
	def readToIntList(self,splitter = " "):
		return list(map(int, self.i.readline().strip('\n').split(splitter)))
	def readToFltList(self,splitter = " "):
		return list(map(float, self.i.readline().strip('\n').split(splitter)))

class Error:
	def __init__(self):
		self.e = sys.stderr
	def write( self, aline ):
		self.e.write(str(aline))
	def writeln(self, aline):
		self.e.write(str(aline) + '\n')

class Solver:
	def __init__(self):
		self.O = Output()
		self.E = Error()
		self.I = Input()
	def solve(self,n):
		return n		

# def permutation(sign,numPosition):
# 	if numPosition == 0:
# 		return []
# 	if numPosition == 1:
# 		return sign
# 	l =[]
# 	for i in range(numPosition):
# 		m = sign[i]
# 		remain =  sign[:i] + sign[i+1:]
# 		for p in permutation(remain,numPosition-1):
# 			l.append([m]+p)
# 	return m

def solve(lists,final):

	'''
	write your code here
	'''
	ans = []
	signs =["+","-","*","/"]
	numPosition = len(lists)-1
	queryList = []
	permutation = itertools.permutations(signs,numPosition)
	for p in permutation:
		cur = ""
		copyL = lists[:]
		p = list(p)
		while len(p) != 0:
			cur += str(copyL.pop(0))
			cur += p.pop(0)
		cur += str(copyL.pop(0))
		queryList.append(cur)
	for q in queryList:
		if final == eval(q):
			ans.append(q)
	return ans




	# return permutation(sign,numPosition)

if __name__ == '__main__':
	O = Output()
	E = Error()
	I = Input()

	query = I.readInt()
	for i in range(query):
		O.writeln(solve(I.readToIntList(),I.readInt()))
