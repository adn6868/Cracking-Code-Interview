from sys import stdin as I
from sys import stdout as O
from sys import stderr as E


def solve(n):
	aset = []
	for char in n:
		if char not in aset:
			aset.append(char)
		else:
			return False
	return True



if __name__ == '__main__':
	q = I.readline()
	for i in range(int(q)):
		O.write (str(solve(I.readline()) )+'\n')
