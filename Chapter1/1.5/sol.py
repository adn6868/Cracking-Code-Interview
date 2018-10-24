from sys import stdin as I
from sys import stdout as O
from sys import stderr as E


def solve(n):
	n = n.replace(" ","%20")
	return n



if __name__ == '__main__':
	q = I.readline()
	for i in range(int(q)):
		O.write (str(solve(I.readline())) +'\n' )