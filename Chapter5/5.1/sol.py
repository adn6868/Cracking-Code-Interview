import sys

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
		return int ( self.i.readline())
	def readFlt( self ):
		return float(self.i.readline())
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

def solve(N,M,i,j):
	'''
	write your code here
	'''
	cur = '1'*i+'0'*(j-i)+'1'*(32-j)
	E.writeln(cur)
	cur = int(cur,2)
	E.writeln(cur)
	cur = cur & N
	E.writeln(bin(cur))
	cur = cur ^ N
	E.writeln(bin(cur))
	M = cur ^ M
	E.writeln((cur))
	return bin(cur)

if __name__ == '__main__':
	O = Output()
	E = Error()
	I = Input()

	query = I.readInt()
	for i in range(query):
		N = int(I.readline(),2)
		M = int(I.readline(),2)
		i = I.readInt()
		j = I.readInt()
		O.write(solve(N,M,i,j)) 
