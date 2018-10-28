import sys
from sys import stdin 
from sys import stdout 
from sys import stderr 

class Output:
	def __init__(self):
		self.o = sys.stdout
	def write( self, aline ):
		self.o.write(str(aline))
	def writeln(self, aline):
		self.o.write(str(aline) + '\n')

class Input:
	def __init__(self):
		self.i = sys.stdin
	def readline( self ):
		return self.i.readline()
	def readInt( self ):
		return int ( self.i.readline())
	def readFlt( self ):
		return float(self.i.readline())
	def readToList(self,splitter = " "):
		return list(self.i.readline().split(splitter))
	def readToIntList(self,splitter = " "):
		return list(map(int, self.i.readline().split(splitter)))
	def readToFltList(self,splitter = " "):
		return list(map(float, self.i.readline().split(splitter)))

class Error:
	def __init__(self):
		self.e = sys.stderr
	def write( self, aline ):
		self.e.write(str(aline))
	def writeln(self, aline):
		self.e.write(str(aline) + '\n')


def solve(n):
	return n
	# E.write(n)


if __name__ == '__main__':
	O = Output()
	E = Error()
	I = Input()

	q = I.readInt()
	for i in range(q):
		O.writeln(solve(I.readToFltList()))
