'''
Me don't know how to write isSubstring
'''
from sys import stdin as I
from sys import stdout as O
from sys import stderr as E

def isSubstring(a,b):
	return b in a or a in b


def solve(a,b):
	return isSubstring(a,a+b+a) and isSubstring(b,b+a+b)
	# E.write(n)


if __name__ == '__main__':
	q = I.readline()
	for i in range(int(q)):
		a = I.readline().strip('\n')
		b = I.readline().strip('\n')
		O.write(str(solve(a,b))+'\n')
